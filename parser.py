from PyPDF2 import PdfReader
import docx

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])