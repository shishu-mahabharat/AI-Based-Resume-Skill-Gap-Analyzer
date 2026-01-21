# 🚀 AI-Based Resume Skill Gap Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NLP](https://img.shields.io/badge/NLP-spaCy-green)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

## 📌 Project Overview
The **AI-Based Resume Skill Gap Analyzer** is an intelligent tool designed to bridge the gap between job seekers and their dream roles. By leveraging **Natural Language Processing (NLP)** and **Machine Learning (ML)**, this system analyzes a candidate's resume against a specific job description (JD), calculates a match percentage, and identifies missing critical skills.

## ❓ Problem Statement
In the modern recruitment process, Applicant Tracking Systems (ATS) filter out millions of resumes based on keyword matching. Many qualified candidates are rejected simply because their resumes lack specific keywords or fail to demonstrate semantic alignment with the job description.

## 💡 Motivation
This project was built to:
- Help candidates optimize their resumes for ATS.
- Provide actionable feedback on missing skills.
- Demonstrate the application of NLP and Vector Space Models in real-world text analysis.

## 🛠️ Tech Stack
- **Programming Language:** Python 3.x
- **NLP Library:** spaCy (for tokenization and phrase matching)
- **Machine Learning:** Scikit-Learn (TF-IDF, Cosine Similarity)
- **Web UI:** Streamlit (for an interactive user interface)
- **Data Handling:** Regular Expressions (Regex)

## 🏗️ System Architecture
1. **Input:** Resume Text & Job Description Text.
2. **Preprocessing:**
   - Lowercasing
   - Special character removal
   - Tokenization & Stopword removal (using spaCy)
3. **Skill Extraction:**
   - Hybrid approach using a predefined skill database and n-gram matching.
4. **Vectorization:**
   - Converting text into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
5. **Similarity Calculation:**
   - Computing **Cosine Similarity** between the resume vector and JD vector.
6. **Output:** Match Score, Matched Skills, Missing Skills, and Recommendations.

## 🧠 NLP & ML Techniques Used
### 1. Text Preprocessing
We use `spaCy` and `regex` to clean the text. This is crucial to remove noise (punctuation, stopwords like "and", "the") so the model focuses only on meaningful words.

### 2. TF-IDF Vectorization
We use **TF-IDF** instead of simple Bag-of-Words because:
- It highlights unique, important words (like specific skills) while down-weighting common words.
- It captures the *importance* of a term in the document relative to the corpus.

### 3. Cosine Similarity
We use **Cosine Similarity** to measure the match.
- It calculates the cosine of the angle between two non-zero vectors.
- **Range:** 0 (No match) to 1 (Perfect match).
- It is preferred over Euclidean distance for text because it is independent of document length (a long resume shouldn't necessarily be "farther" from a short JD).

## 🚀 How to Run the Project

### Prerequisites
- Python 3.8+ installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-skill-gap-analyzer.git
   cd resume-skill-gap-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Running the CLI Version
```bash
python src/main.py
```

### Running the Streamlit UI
```bash
streamlit run src/app.py
```

## 📊 Sample Output
**Resume Match Score:** 78%

**Matched Skills:**
- Python
- Machine Learning
- SQL

**Missing Skills:**
- Docker
- AWS

**Recommendation:**
*Good match, but you are missing some key skills like Docker, AWS. Consider learning these.*

## ⚠️ Limitations
- The current skill database is manual and may not cover every niche technology.
- Contextual understanding (e.g., distinguishing "Java" coffee vs. language) relies on the specific domain of the text.
- TF-IDF ignores word order (semantic meaning is partially lost compared to BERT/Embeddings).

## 🔮 Future Enhancements
- **BERT/Transformers:** Use SBERT for better semantic similarity.
- **Named Entity Recognition (NER):** Train a custom NER model to extract skills automatically without a list.
- **Cloud Integration:** Deploy on AWS/Azure for public access.

---
*Built with ❤️ by [Your Name]*
