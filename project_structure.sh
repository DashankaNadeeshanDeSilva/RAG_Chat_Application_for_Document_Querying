RAG-Chat-Application/
├── backend/
│   ├── Dockerfile                           
│   ├── requirements.txt                        
│   ├── app/
│   │   ├── services/
│   │   │   │── document_preprocessing/
│   │   │   │── chat_histroy.py
│   │   │   │── knowledge_base.py     
│   │   │   │── llm_service.py     
│   │   │   │── rag.py                   
│   │   ├── vector_db
│   │   ├── main.py
│   ├── tests/
├── frontend/
│   ├── Dockerfile 
│   │   ├── src/               
│   │   │   ├── app.js 
│   │   │   ├── html.index 
│   │   │   ├── styles.css 
├── .env                                   
├── images/  
├── uploads/                   
└── docker-compose.yml                            
