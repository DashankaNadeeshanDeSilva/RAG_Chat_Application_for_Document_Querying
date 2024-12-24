from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.data_processing.process_documents import process_documents

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
        # Get document content
        content = await file.read()
        # process the document
        process_documents(content)
        # try to return a sucess code to check if document
        # is processed successfully (preprocessed and added to vector db)

        return {"message": "File processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat/")
async def chat_query(query: str = Form(...)):

    try:
        # Preprocess the query
        cleaned_query = query.strip()
        # query the vector database
        retrived_context = query_knowledge_base(cleaned_query)
        # generate final response
        response = generate_response(query, retrived_context)

        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))