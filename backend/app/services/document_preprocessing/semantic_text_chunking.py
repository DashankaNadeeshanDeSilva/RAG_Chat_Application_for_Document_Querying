import spacy
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

def semantic_text_chunking_with_spacy(text: str, max_tockens: int = 100) -> List[str]:
    """
    Semantic chunking, splits the text into semantically meaningful chunks
    and ensures each chunk preserves its context and 
    avoids splitting across semantically meaningful boundaries.
    
    args:
        text (str): cleaned text from documents
        max_tokens (int): maximum num of tockens for each chunk
    return
        List[str]: list of chunks (str)
    """

    nlp_module = spacy.load("en_core_web_sm") # assume english documents only
    document = nlp_module(text)
    chunks = []
    current_chunk = []
    current_chunk_length = 0

    for sentences in document.sents:
        tokens = len(sentences)
        if current_chunk_length + tokens > max_tockens:
            chunks.append(" ".join(current_chunk))
            current_length += tokens

    if current_chunk:  # Add the remaining chunk
        chunks.append(" ".join(current_chunk))

    return chunks


def semantic_text_chunking(text: str) -> List[str]:
    # Initialize the SemanticChunker with OpenAI embeddings
    text_splitter = SemanticChunker(OpenAIEmbeddings())

    # Split into semantically meaningful chunks
    doc_chunks = text_splitter.create_documents([text])

    chunks = [chunk.page_content for chunk in doc_chunks]
    # meta_data = [chunk_metadata.metadata for chunk_metadata in doc_chunks] # chunk_metadata is a dict
    return chunks

