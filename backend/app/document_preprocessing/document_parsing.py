import os
from PyPDF2 import PdfReader
from docx import Document

class Document_Parsing:
    def __init__(self):
        pass
        
    def __call__(self, file_path: str) -> str:
        """
        parse documents and extracts raw text.
        args: 
            file_path (str): file path to the document.
        returns: 
            str: extracted raw text from document.
        """
        _, file_extention = os.path.splitext(file_path)

        # check file extention and parse
        if file_extention.lower() == ".pdf":
            try:
                return self.parse_pdf(file_path)
            except Exception as e:
                return f"Error parsing file {file_path}: {str(e)}"
        elif file_extention.lower() == ".docx":
            try:
                return self.parse_docx(file_path)
            except Exception as e:
                return f"Error parsing file {file_path}: {str(e)}"
        elif file_extention.lower() == ".txt":
            try:
                return self.parse_txt(file_path)
            except Exception as e:
                return f"Error parsing file {file_path}: {str(e)}"
        else:
            raise ValueError(f"Unsupported document format: {file_extention}; supported formats: pdf, docx and txt.")
            # Find a way to not to let the application stop/crash just because a file with wrong format has been uploaded and work the way/continue bypassing this issue
        
    def parse_pdf(self, file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    def parse_docx(self, file_path: str) -> str:
        document = Document(file_path)
        text = '\n'.join([paragraph.text for paragraph in document.paragraphs])
        return text
    
    def parse_txt(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text


    


