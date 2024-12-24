from bertopic import BERTopic
from keybert import KeyBERT

def add_metadata(chunks: List[str]) -> List[dict]:
    """
    generate metadata as topics and keywords for each chunk
    args:
        chunks (List[str]): List of text chunks (str)
    retun:
        List[dict]: list of dictoneries with chunks and metadata for each element
    """

    # topic modeling
    topic_model = BERTopic()
    topics, probs = topic_model.fit_transform(chunks) # input: list of docs(str)
    metadata = []

    # keywords extraction
    kw_model = KeyBERT()

    for chunk, topic in zip (chunks, topics):
        chunk_keywords = kw_model.extract_keywords(chunk, keyphrase_ngram_range=(1, 2), stop_words='english')
        chunk_keywords = [kw[0] for kw in chunk_keywords]
        
        if topic != -1:  # Check if a valid topic is assigned
            chunk_topic = topic_model.get_topic(topic)
            chunk_topic = " ".join([topic[0] for topic in chunk_topic])
        else:
            chunk_topic = "No topic assigned"
        
        metadata.append({
            "chunk": chunk,
            "topic": chunk_topic,
            "keywords": chunk_keywords
        })
