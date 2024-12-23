from document_parsing import Document_Parsing
from clean_text import clean_text
from semantic_text_chunking import semantic_text_chunking
# from backend.document_preprocessing.add_metadata import generate_metadata
from add_metadata import add_metadata

def preprocess_document(file_path: str): # -> List[dict]
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
    raw_text = document_parser(file_path)

    # step 2: clean text
    clean_text = clean_text(raw_text)

    # step 3: semantic chunking
    text_chunks = semantic_text_chunking(clean_text)

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