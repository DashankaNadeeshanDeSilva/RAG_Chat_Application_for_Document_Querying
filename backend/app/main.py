from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
#from app.document_preprocessing.preprocessing_pipeline import preprocess_document

app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to the domain of your frontend in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx", ".txt")):
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    try:
        content = await file.read()
        #result = preprocess_document(file.file)
        result = "This is the so called document !"
        return {"message": "File processed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat/")
async def chat_query(query: str = Form(...)):
    # Use the RAG pipeline to process the query
    response = {"response": f"I read your message: {query}"}
    return response
