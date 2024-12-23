import re

def clean_text(text: str) -> str:
    """
    Clean text by removing unwanted characters and normalizing the format
    args:
        text (str): raw text from document
    return:
        text (str): cleaned text
    """

    # Replace multiple spaces and newlines (\n) with a single space
    text = re.sub('\n', '', text)
    text = re.sub(' +', ' ', text)
    # Remove special characters except punctuation
    text = re.sub(r'[^\w\s.,!?]', '', text) 
    # remove leading and trailing spaces
    text = text.strip()

    return text
