import streamlit as st
from preprocess import preprocess_text
from skill_extractor import extract_skills
from similarity import calculate_similarity
from utils import extract_text_from_file

def get_recommendation(score, missing_skills):
    if score >= 80:
        return "Excellent match! Your profile aligns well with the job description."
    elif score >= 50:
        if missing_skills:
            return f"Good match, but you are missing some key skills like {', '.join(list(missing_skills)[:3])}."
        else:
            return "Good match. Focus on quantifying your achievements."
    else:
        return "Low match. Tailor your resume or acquire missing skills."

st.set_page_config(page_title="Resume Skill Gap Analyzer", layout="wide")

st.title("AI-Based Resume Skill Gap Analyzer 🚀")
st.markdown("Compare your resume with a job description to find skill gaps and improve your chances.")

col1, col2 = st.columns(2)

resume_text = ""
jd_text = ""

with col1:
    st.subheader("Resume")
    resume_file = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf", "txt"])
    if resume_file:
        resume_text = extract_text_from_file(resume_file)
        st.success("Resume uploaded successfully!")
        with st.expander("Show Extracted Resume Text"):
            st.text(resume_text)
    else:
        resume_text = st.text_area("Or Paste Resume Text", height=300, placeholder="Paste your resume here...")

with col2:
    st.subheader("Job Description")
    jd_file = st.file_uploader("Upload Job Description (PDF/TXT)", type=["pdf", "txt"])
    if jd_file:
        jd_text = extract_text_from_file(jd_file)
        st.success("JD uploaded successfully!")
        with st.expander("Show Extracted JD Text"):
            st.text(jd_text)
    else:
        jd_text = st.text_area("Or Paste Job Description", height=300, placeholder="Paste the JD here...")

if st.button("Analyze Resume"):
    if resume_text and jd_text:
        with st.spinner("Analyzing..."):
            # Preprocess
            processed_resume = preprocess_text(resume_text)
            processed_jd = preprocess_text(jd_text)
            
            # Similarity
            score, percentage = calculate_similarity(processed_resume, processed_jd)
            
            # Skills
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)
            
            matched_skills = resume_skills.intersection(jd_skills)
            missing_skills = jd_skills.difference(resume_skills)
            
            # Display Results
            st.divider()
            st.header(f"Match Score: {percentage}%")
            st.progress(int(percentage))
            
            rec = get_recommendation(percentage, missing_skills)
            st.info(f"💡 Recommendation: {rec}")
            
            # Debugging/Transparency Section
            with st.expander("📊 See Detailed Skill Extraction Analysis", expanded=False):
                d_col1, d_col2 = st.columns(2)
                with d_col1:
                    st.write(f"**Skills found in Resume ({len(resume_skills)}):**")
                    st.write(", ".join(resume_skills) if resume_skills else "No skills detected")
                with d_col2:
                    st.write(f"**Skills found in JD ({len(jd_skills)}):**")
                    st.write(", ".join(jd_skills) if jd_skills else "No skills detected")
                    
            if not jd_skills:
                st.warning("⚠️ No technical skills were detected in the Job Description. This is why 'Missing Skills' shows 'None'. Please check if the JD text was extracted correctly.")

            row1_col1, row1_col2 = st.columns(2)
            
            with row1_col1:
                st.success(f"✅ Matched Skills ({len(matched_skills)})")
                if matched_skills:
                    for skill in matched_skills:
                        st.write(f"- {skill}")
                else:
                    st.write("None")
                    
            with row1_col2:
                st.error(f"⚠️ Missing Skills ({len(missing_skills)})")
                if missing_skills:
                    for skill in missing_skills:
                        st.write(f"- {skill}")
                else:
                    if not jd_skills:
                        st.write("*(No skills to miss - JD extraction failed)*")
                    else:
                        st.write("None (You have all the required skills!)")
    else:
        st.warning("Please provide both Resume and Job Description text.")
