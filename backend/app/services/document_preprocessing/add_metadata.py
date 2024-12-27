from bertopic import BERTopic
from keybert import KeyBERT
from typing import List

def add_metadata(chunks: List[str]) -> List[dict]:
    """
    generate metadata as topics and keywords for each chunk
    args:
        chunks (List[str]): List of text chunks (str)
    retun:
        List[dict]: list of dictoneries with chunks and metadata for each element
    """
    if len(chunks) < 2:
        raise ValueError("Not enough chunks for topic modeling. Provide at least 2 chunks.")

    # topic modeling
    topic_model = BERTopic(min_topic_size=2, nr_topics="auto", verbose=True)
    try: 
        topics, probs = topic_model.fit_transform(chunks) # input: list of docs(str)
    except ValueError as e:
        raise RuntimeError("Topic modeling failed. Ensure chunks are of sufficient size.") from e

    metadata = []

    # keywords extraction
    kw_model = KeyBERT()

    #for chunk, topic in zip (chunks, topics):
    for idx, (chunk, topic) in enumerate(zip(chunks, topics)):
        # Extract keywords from chunks
        try:
            chunk_keywords = kw_model.extract_keywords(chunk, keyphrase_ngram_range=(1, 2), stop_words='english')
            chunk_keywords = [kw[0] for kw in chunk_keywords]
        except:
            chunk_keywords = ["No KWs"] # fallback in case kw extraction fails
        
        # Assign topics to chunks
        if topic != -1:  # Check if a valid topic is assigned
            try:
                chunk_topic = topic_model.get_topic(topic)
                if chunk_topic:
                    chunk_topic = " ".join([topic[0] for topic in chunk_topic[:10]])+str(idx)
                else:
                    chunk_topic = " ".join(chunk_keywords)+str(idx)
            except IndexError:
                chunk_topic = "Miscellaneous"+str(idx)  # Fallback for invalid topic ID

        else:
            chunk_topic = " ".join(chunk_keywords)+str(idx) if chunk_keywords else "No topic assigned"+str(idx)
        
        metadata.append({
            "chunk": chunk,
            "topic": chunk_topic,
            "keywords": chunk_keywords
        })
    
    return metadata
