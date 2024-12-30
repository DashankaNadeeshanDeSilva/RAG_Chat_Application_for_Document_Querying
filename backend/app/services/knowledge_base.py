import chromadb
from chromadb.utils import embedding_functions
from typing import List

class Knowledge_Base():
    def __init__(self, db_path="app/vector_db/"):
        self.db_path = db_path
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    def get_collection(self, collection_name="knowledge_base"):
        collection = self.client.get_collection(collection_name)
        return collection # ChromaDB collection object.
    
    def get_or_create_collection(self, collection_name="knowledge_base"):
        collection = self.client.get_or_create_collection(
             name=collection_name, 
             embedding_function=self.embedding_func)
        return collection # ChromaDB collection object.

    def add_to_collection(self, collection, document):
        '''documnets format (List[dict]), e.g. [{"chunk":"foo","topic":"bar", "keywords": ["kw1,"kw2"]}
        '''
        if not isinstance(document, list) or not all(isinstance(item, dict) for item in document):
            raise ValueError("Documents must be a list of dictionaries.")

        doc_chunks = [doc_chunk["chunk"] for doc_chunk in document] # document
        doc_topics = [doc_topic["topic"] for doc_topic in document] # ids
        doc_kws = [doc_kw["keywords"] for doc_kw in document] # metadata

        collection.add(
            documents=doc_chunks,
            ids=doc_topics
        )
        print("SUCCESSFULLY ADDED TO VECTOR DB !")

    def query_collection(self, collection, query, n_results=5):
        results_raw = collection.query(query_texts=[query], n_results=n_results)
        results = [str(result) for result in results_raw["documents"][0]]
        return results
    
    def clear_collection(self, collection):
        all_docs = collection.get()
        collection.delete(ids=all_docs['ids']) 

     