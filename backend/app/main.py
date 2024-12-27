from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.rag import process_documents, generate_rag_response, create_or_clear_db
import os


app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "./uploads"

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

        '''# Get document content
        content = await file.read()
        # process the document and store in vector db
        process_documents(content)'''

        return {"message": "File processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/")
async def chat_query(query: str = Form(...)):
    try:
        # generate response for query
        response = generate_rag_response(query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))