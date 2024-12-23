# RAG_Chat_Interface_for_document_querying
RAG Chat application to ask and query uploaded documents.

The RAG chatbot application should be a chat conversation app with frontend and backend where frontend is a chat interface where user can chat and also uploade documents to the knowledge base. The reply for user chat query should display as reply chat on the chat interface.

Here is the workflow of the RAG chatbot:

1. Input documents and preprocessing: 
- This step includes steps parsing documents, cleaning the, and chunking or splitting break down documents into smaller, manageable chunks.
- The chunks should be meaningful, not splitting across important boundaries.
- Then meta data addition such as titles and tags to those chucnks to provide context.

2. Creating a Knowledge base:
- Use a pre-trained text embedding model (open source) to convert each chunk in to embeddings.
- The store these embeddings with their corresponing meta data and original text in vector database (Chromadb)

3. Indexing Documents for efficient similarity search
- Vector Indexing: Organize the embeddings using nearest-neighbor algorithms (e.g., HNSW or IVFPQ) to enable fast retrieval based on semantic similarity.
- Metadata Indexing (Optional): Index metadata fields separately for advanced filtering during retrieval (e.g., retrieving chunks by date or author).

4. Querying the Knowledge Base:
- Input Query: A user submits a natural language query that needs context or answers in the chatbot
- Create set of keywords using LLM that is relevent to query that carries same semantics for better similarity search
- Query Embedding: Convert the user's query into a semantic embedding using the same text embedding model used for the documents.
- Keyword Embeddings: Convert generated helper keywords also into semantic embeddings

5. Similarity Search:
Use the query embeddings to search the vector database for the most semantically similar document chunks. The database retrieves the top-N chunks based on cosine similarity or other distance metrics.

5. Generating Context-Aware Responses
- Combine Context: The retrieved document chunks (context) are combined with the user query. This combination forms the input for the language model.
- LLM Generation: Pass the combined input to a pre-trained LLM. The LLM generates a response that incorporates the retrieved context to provide more accurate and relevant answers.

6. Reply to the user
- The genarated natural language response is sent back to the user as reply in the chatbot.
