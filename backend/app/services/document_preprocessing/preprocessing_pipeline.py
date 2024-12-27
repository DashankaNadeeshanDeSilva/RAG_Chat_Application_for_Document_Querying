# from document_parsing import Document_Parsing
from backend.app.services.document_preprocessing.get_content import get_content
from backend.app.services.document_preprocessing.clean_text import clean_text
from backend.app.services.document_preprocessing.semantic_text_chunking import semantic_text_chunking
from backend.app.services.document_preprocessing.add_metadata import add_metadata
from backend.app.services.document_preprocessing.document_parsing import Document_Parsing
from typing import List

def preprocess_document(document_path: str) -> List[dict]:
    """
    intergrate components of text perprocessing
    args:
        file_path (str)
    return:
        List[dict]: list of dict, each include chunk and metadata (topic and keywords)
        dict keys: chunk, topic, keywords
    """

    # step 1: document parsing
    document_parser = Document_Parsing()
    raw_text = document_parser(document_path)
    #raw_text = get_content(document)

    # step 2: clean text
    cleaned_text = clean_text(raw_text)

    # step 3: semantic chunking
    text_chunks = semantic_text_chunking(cleaned_text)

    # step 4: metadata generation and integrate
    preprocessed_text = add_metadata(text_chunks)

    return preprocessed_text


# Example usage
if __name__ == "__main__":
    file_path = "path/to/your/sample.pdf"
    try:
        output = preprocess_document(file_path)
        for item in output:
            print(f"Chunk: {item['chunk']}")
            print(f"Topic: {item['topic']}")
            print(f"Keywords: {', '.join(item['keywords'])}\n")
    except Exception as e:
        print(f"Error: {e}")