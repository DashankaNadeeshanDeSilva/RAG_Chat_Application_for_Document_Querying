from backend.app.services.knowledge_base.knowledge_base import Knowledge_Base
from backend.app.services.document_preprocessing.preprocessing_pipeline import preprocess_document

def process_documents(document: bytes):
    # prepocess document
    preprocessed_text = preprocess_document(document) # List[dict]
    # Adding the document to knowledgebase
    knowledge_base = Knowledge_Base()
    knowledge_base_collection = knowledge_base.get_collection()
    knowledge_base.add_to_collection(knowledge_base_collection, preprocessed_text)


# def create_additional_keywords() 


def query_knowledge_base(query: str) -> List[str]:
    # preprocess the query
    query = query.strip()

    # add additional keywords
    query_kw = add_keywords(query)

    # query from the knowledgebase
    knowledge_base = Knowledge_Base()
    knowledge_base_collection = knowledge_base.get_collection()
    retrieved_context = query(knowledge_base_collection, query_kw)
    
    return retrieved_context
