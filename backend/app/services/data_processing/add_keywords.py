from backend.app.services.data_processing.llm_service import LLM

def add_keywords(query: str) -> str:

    # {query} keywords: kw1, kw2, kw3
    prompt = f"Generate 10 semantic, relevant two-word keywords related to the query for context retrieval in a RAG system. Output keywords only. \nQuery: {query}"
    llm = LLM()
    kws = llm.invoke_llm(prompt)
    query_with_kws = query + str(kws)

    return query_with_kws