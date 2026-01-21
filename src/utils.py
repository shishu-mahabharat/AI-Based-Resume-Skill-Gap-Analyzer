from pdfminer.high_level import extract_text
import io

def extract_text_from_pdf(pdf_source):
    """
    Extracts text from a PDF file.
    
    Args:
        pdf_source: File path (str) or file-like object (BytesIO).
        
    Returns:
        str: Extracted text.
    """
    try:
        return extract_text(pdf_source)
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_file(uploaded_file):
    """
    Extracts text from an uploaded file (PDF or TXT).
    
    Args:
        uploaded_file: Streamlit UploadedFile object.
        
    Returns:
        str: Extracted text.
    """
    try:
        if uploaded_file.name.endswith('.pdf'):
            return extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith('.txt'):
            return uploaded_file.read().decode("utf-8")
        else:
            return "Unsupported file format."
    except Exception as e:
        return f"Error reading file: {str(e)}"
