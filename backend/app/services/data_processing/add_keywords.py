
def add_keywords(query: str) -> str:

    # {query} keywords: kw1, kw2, kw3
    kws = invoke_llm(query, prompt)
    query_with_kws = query + str(kws)

    return query_with_kws