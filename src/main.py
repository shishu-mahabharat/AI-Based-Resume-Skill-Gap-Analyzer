import os
import sys
from preprocess import preprocess_text
from skill_extractor import extract_skills
from similarity import calculate_similarity
from utils import extract_text_from_pdf

def read_file(file_path):
    try:
        if file_path.lower().endswith('.pdf'):
            return extract_text_from_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

def get_recommendation(score, missing_skills):
    if score >= 80:
        return "Excellent match! Your profile aligns well with the job description. Highlight your projects."
    elif score >= 50:
        if missing_skills:
            return f"Good match, but you are missing some key skills like {', '.join(list(missing_skills)[:3])}. Consider learning these."
        else:
            return "Good match. Focus on quantifying your achievements in the resume."
    else:
        return "Low match. You might want to tailor your resume more significantly or acquire the missing skills."

def main():
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_path = os.path.join(base_dir, 'data', 'sample_resume.txt')
    jd_path = os.path.join(base_dir, 'data', 'sample_job_description.txt')
    
    print("--- AI-Based Resume Skill Gap Analyzer ---")
    print("Reading files...")
    
    resume_text = read_file(resume_path)
    jd_text = read_file(jd_path)
    
    print("Preprocessing text...")
    processed_resume = preprocess_text(resume_text)
    processed_jd = preprocess_text(jd_text)
    
    print("Extracting skills...")
    resume_skills = extract_skills(resume_text) # Extract from original text for better matching usually, or processed?
    # Our extract_skills uses n-gram on lowercased text, so original text is fine (it handles lowercasing internally)
    jd_skills = extract_skills(jd_text)
    
    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)
    
    print("Calculating similarity...")
    score, percentage = calculate_similarity(processed_resume, processed_jd)
    
    recommendation = get_recommendation(percentage, missing_skills)
    
    # Output
    print("\n" + "="*30)
    print(f"Resume Match Score: {percentage}%")
    print("="*30)
    
    print("\nMatched Skills:")
    if matched_skills:
        for skill in matched_skills:
            print(f"- {skill}")
    else:
        print("- None")
        
    print("\nMissing Skills:")
    if missing_skills:
        for skill in missing_skills:
            print(f"- {skill}")
    else:
        print("- None")
        
    print(f"\nRecommendation:\n{recommendation}")
    print("="*30)

if __name__ == "__main__":
    main()
