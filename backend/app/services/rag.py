from backend.app.services.knowledge_base import Knowledge_Base
from backend.app.services.document_preprocessing.preprocessing_pipeline import preprocess_document
from backend.app.services.llm_service import LLM
from typing import List

### Core functions of RAG ###

# Add keywords to query
def add_keywords(query: str) -> str:
    # {query} keywords: kw1, kw2, kw3
    prompt = f"Generate 10 semantic, relevant two-word keywords related to the query for context retrieval in a RAG system. Output keywords only. \nQuery: {query}"
    llm = LLM()
    kws = llm.invoke_llm(prompt)
    query_with_kws = query + str(kws)
    return query_with_kws


# Preprocess and store document in vecotr db
def process_documents(file_path: str):
    # prepocess document
    preprocessed_text = preprocess_document(file_path) # List[dict]
    # Adding the document to knowledgebase
    knowledge_base = Knowledge_Base()
    knowledge_base_collection = knowledge_base.get_collection()
    knowledge_base.add_to_collection(knowledge_base_collection, preprocessed_text)



# Query for context given query
def query_knowledge_base(query: str) -> List[str]:
    # preprocess the query
    query = query.strip()
    # add additional keywords to query
    query_kw = add_keywords(query)
    # query from the knowledgebase
    knowledge_base = Knowledge_Base()
    knowledge_base_collection = knowledge_base.get_collection()
    retrieved_context = knowledge_base.query_collection(knowledge_base_collection, query_kw)
    return retrieved_context


# Generate rag output response
def generate_rag_response(query: str, chat_history: str) -> str:
    context = query_knowledge_base(query)
    prompt = f"""Given the query and context, generate a consise, clear and organized natural language response:\nQuery: {query}\nContext: {context}.\n 
     Use follwoing chat histroy too: \nchat histoy: {chat_history}"""
    llm = LLM()
    rag_response = llm.invoke_llm(prompt)
    return rag_response


# Check and clear or create vector db at app startup
def create_or_clear_db(collection_name="knowledge_base"):
    knowledge_base = Knowledge_Base()
    # check if collection exists, then get it, if not create a new one
    try:
        collection = knowledge_base.get_or_create_collection(collection_name) 
        if collection.count() != 0:
            knowledge_base.clear_collection(collection)
    except Exception as e:
        print(f"Error during vector database initialization: {str(e)}")
