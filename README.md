
# RAG Chat Application for Document Knowledge Querying
### An interactive RAG application chatbot where users can upload documents, and query from them to get context and extract knowledge.

This RAG Chatbot Application features a user-friendly front end and a Large Language Model (LLM) powered back end. The front end provides an interactive chat interface, allowing users to engage in real-time conversations and upload documents to enrich the knowledge base. The back end powers the application by handling essential data processing tasks, including document indexing in a vector database, querying the database for relevant information, and generating context-aware responses using an LLM.

## The RAG chat application architecture:

![RAG_architecture.jpg](images/RAG_architecture.jpg)

## RAG chat application workflow:

1. Input Documents and Preprocessing
- Parse, clean, and split documents into smaller, meaningful chunks, ensuring no important boundaries are disrupted.
- Add metadata: titles (topic modelling), and keywords to the chunks to provide contextual information.

2. Creating the Knowledge Base
- Use an open-source pre-trained text embedding model to convert each document chunk into embeddings.
- Store these embeddings, along with their metadata and original text, in a vector database (e.g., ChromaDB).

3. Querying the Knowledge Base
- User Query: The user submits a natural language query.
- Keyword Generation: Generate semantic keywords from the query using an LLM for improved similarity search (Additional task compared to conventional RAG workflow).
- Embedding Creation: Convert both the query and generated keywords into embeddings using the same embedding model used for the documents.

4. Similarity Search
- Perform a similarity search in the vector database using query embeddings.
- Retrieve the top-N most relevant document chunks based on cosine similarity or other metrics.

5. Generating Context-Aware Responses
- Combine Context: Merge the retrieved document chunks with the user query to form the input for the LLM.
- LLM Response: Generate a contextually accurate response using a pre-trained LLM.
- Maintain a conversation history to provide continuity across the dialogue.

6. Reply the User in the chat
- Send the LLM-generated response back to the user as a natural language reply in the chat interface.

## Technologies Used
- Data Preprocessing: Spacy, Sentence Transformers, BERTopic and KeyBERT
- LLM: Llama 3.2 3b-instruct via OpenRouter API (Free)
- Vector DB: Chromadb
- Chat Interface: JavaScript and HTML
- Application: FastAPI
- Deployment: Docker

## How to Run Locally
1. Install dependencies (in the `backend` dir):
   ```bash
   pip install -r requirements.txt
   ```
2. (a) Run the frontend and backend seperately:
- Backend (change to `backend` dir)
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
- Frontend (change to `frontend/src` dir)
    ```
    python -m http.server 8080
    ```
2. (b) Run with Docker Compose file:
- Docker compose file orchestrates both frontend and backend Docker containers (Docker should be installed)
    ```
    docker-compose up --build
    ```

## Deploy in Cloud

Deploy with Docker (for Linux/macOS) in an AWS EC2 instance:

1. Create an AWS EC2 Instance and running with SSH access.

2. Create and download SSH Key Pair (.pem file) associated with your EC2 instance.

3. Install Docker and Docker Compose on your local machine and EC2 instance. 

4. Create an IAM Role with `AmazonEC2ContainerRegistryFullAccess` policy and attach with the EC2 
instance.

5. Configure the local machine: Adjust permissions of the Key Pair file (navigate to its location).
   ```bash 
   chmod 400 your-key.pem
   ``` 

6. Connect to the EC2 instance using SSH.
   ```bash 
   ssh -i "your-key.pem" ubuntu@<EC2-Public-IP>
   ```
7. Navigate to a desired dir inside EC2 instance (e.g. `cd /home/ubuntu`) and clone this project repo.
   ```
   git clone <repository-url>
   ```
   Otherwise, first clone the repo to the local machine and then transfer to the EC2 instance.
   ```bash 
   scp -i "your-key.pem" -r <RAG application repo> ubuntu@<EC2-Public-IP>:/home/ubuntu/
   ```

8. Navigate into project dir and run the application by running the Docker Compose file.
    ```
    docker-compose up --build
    ```
   The RAG application is now running in the EC2 instance as a Docker container. Access it via `http://<EC2-Public-IP>:80`


## Potential Use Cases:
- Academic research assistants.
- Legal document review and querying.
- Customer support knowledge bases.
- Enterprise document search tools.

## Final Remarks:
This project was conducted as a learning exercise to build an RAG chat application. Feel free to create an issue if you find any problems or feedback (both positive and negative). Thank you for checking this repository out.
