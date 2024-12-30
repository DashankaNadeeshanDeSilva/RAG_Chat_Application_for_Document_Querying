from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from app.services.rag import process_documents, generate_rag_response, create_or_clear_db
from app.services.chat_histroy import update_chat_history
import os
from uuid import uuid4


app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "./uploads"
chat_histories = {}  # Example: {user_id: [{'role': 'user', 'content': '...'}, {'role': 'bot', 'content': '...'}]}


@app.on_event("startup")
def startup_event():
    try:
        # Create uploads directory if it doesn't exist
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
            print(f"Directory '{UPLOAD_DIR}' created for file uploads.")

        create_or_clear_db(collection_name="knowledge_base")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx", ".txt")):
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    try:
        file_path = f"./uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        process_documents(file_path)

        return {"message": "File processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/")
async def chat_query(query: str = Form(...), user_id: str = Form(...)):
    try:
        print(f"Query: {query}, User ID: {user_id}")

        # Initialize user chat history if it doesn't exist
        if user_id not in chat_histories:
            chat_histories[user_id] = []
        
        # generate response for query
        response = generate_rag_response(query=query, chat_history=chat_histories[user_id])

        # Update chat history  for user and bot after generating the response
        update_chat_history(
            chat_histories=chat_histories, 
            user_id=user_id, 
            user_content=query,
            bot_content=response
        )
        return {"response": response}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/start_session/")
def start_session():
    # Generates and returns a unique session_id.
    session_id = str(uuid4())
    return {"session_id": session_id}