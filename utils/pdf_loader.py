"""
PDF Loader Utility:
Extracts plain text from PDF.
"""

import PyPDF2

def extract_text_from_pdf(file) -> str:
    """
    Extract text from uploaded PDF file.
    """
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
