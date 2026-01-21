import spacy
import re
import sys
import subprocess

# Ensure spacy model is downloaded
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    """
    Preprocesses the input text by:
    1. Lowercasing
    2. Removing special characters and numbers (keeping only alphabets and spaces)
    3. Removing extra whitespace
    
    Args:
        text (str): Raw input text.
        
    Returns:
        str: Cleaned text.
    """
    # 1. Lowercasing
    text = text.lower()
    
    # 2. Remove special characters, punctuation, and numbers (keep only letters and spaces)
    # This regex replaces anything that is NOT a letter or whitespace with a space
    text = re.sub(r'[^a-z\s]', ' ', text)
    
    # 3. Remove extra whitespace (multiple spaces becomes single space)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def preprocess_text(text: str) -> str:
    """
    Advanced preprocessing using spaCy:
    1. Tokenization
    2. Stopword removal
    3. Lemmatization (optional but good for matching)
    
    Args:
        text (str): Raw input text.
        
    Returns:
        str: Preprocessed text (tokens joined back to string).
    """
    # First apply basic cleaning
    cleaned_text = clean_text(text)
    
    # Process with spaCy
    doc = nlp(cleaned_text)
    
    # Filter tokens:
    # - remove stopwords
    # - remove punctuation (already mostly handled by regex, but good to be safe)
    # - remove empty strings
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.text.strip()]
    
    return " ".join(tokens)

if __name__ == "__main__":
    # Test the module
    sample_text = "Python is a great programming language! I love Machine Learning."
    print(f"Original: {sample_text}")
    print(f"Processed: {preprocess_text(sample_text)}")
