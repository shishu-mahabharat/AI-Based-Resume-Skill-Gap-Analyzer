from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Tuple

def calculate_similarity(resume_text: str, jd_text: str) -> Tuple[float, float]:
    """
    Computes the semantic similarity between the resume and job description using TF-IDF and Cosine Similarity.
    
    Why TF-IDF?
    - It increases the weight of terms that are specific to the documents (like rare technical skills) 
      and decreases the weight of common words.
      
    Why Cosine Similarity?
    - It measures the cosine of the angle between two vectors. It is effective for text similarity 
      as it is independent of the document length.
    
    Args:
        resume_text (str): Preprocessed resume text.
        jd_text (str): Preprocessed job description text.
        
    Returns:
        float: Similarity score (0.0 to 1.0).
        float: Similarity percentage (0.0 to 100.0).
    """
    
    # Create the Document Term Matrix
    corpus = [resume_text, jd_text]
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the corpus
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Compute Cosine Similarity
    # tfidf_matrix[0] is the resume vector
    # tfidf_matrix[1] is the JD vector
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    # Extract the score
    similarity_score = similarity_matrix[0][0]
    similarity_percentage = round(similarity_score * 100, 2)
    
    return similarity_score, similarity_percentage

if __name__ == "__main__":
    r = "python machine learning data science"
    j = "looking for python data science expert"
    score, pct = calculate_similarity(r, j)
    print(f"Match: {pct}%")
