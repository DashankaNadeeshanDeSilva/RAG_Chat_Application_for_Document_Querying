import spacy
import spacy.cli
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from typing import List
from sentence_transformers import SentenceTransformer

def semantic_text_chunking(text: str, max_tokens: int = 100) -> List[str]:
    """
    Semantic chunking using spaCy, splits the text into semantically meaningful chunks
    and ensures each chunk preserves its context and avoids splitting across semantically meaningful boundaries.
    
    args:
        text (str): cleaned text from documents
        max_tokens (int): maximum number of tokens for each chunk
    return:
        List[str]: list of semantically meaningful text chunks
    """
    # Load the spaCy model (English by default)
    nlp = spacy.load("en_core_web_sm")
    document = nlp(text)

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in document.sents:  # Process each sentence in the document
        sentence_length = len(sentence.text.split())  # Count tokens in the sentence
        if current_length + sentence_length > max_tokens:
            # Add the current chunk and reset
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        
        current_chunk.append(sentence.text)
        current_length += sentence_length

    if current_chunk:  # Add the last remaining chunk
        chunks.append(" ".join(current_chunk))

    return chunks

'''
def semantic_text_chunking(text: str) -> List[str]:

    # Initialize custom embeddings
    custom_embeddings = CustomEmbeddings()

    # Initialize the SemanticChunker with  custom embeddings
    text_splitter = SemanticChunker(embeddings=custom_embeddings)

    # Split into semantically meaningful chunks
    doc_chunks = text_splitter.create_documents([text])
    chunks = [chunk.page_content for chunk in doc_chunks]
    # meta_data = [chunk_metadata.metadata for chunk_metadata in doc_chunks] # chunk_metadata is a dict
    
    return chunks


class CustomEmbeddings:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        return self.model.encode(texts, convert_to_tensor=True).tolist()
    
    def embed_documents(self, texts):
        """
        Required by SemanticChunker: Embeds a list of texts into document embeddings.
        :param texts: List of input texts to embed.
        :return: List of embeddings as vectors.
        """
        return self.embed(texts)
'''