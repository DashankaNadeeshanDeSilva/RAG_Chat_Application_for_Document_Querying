# from base package
FROM python:3.10-slim

# Set environment variables
# Ensure Python output is logged immediately
ENV PYTHONUNBUFFERED=1  
# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1  


# Set working dir inside the container
WORKDIR /RAG_app

# install dependencies
COPY backend/requirements.txt /RAG_app/requirements.txt
RUN pip install --no-cache-dir -r /RAG_app/requirements.txt

# Copy backend files to the container working dir
COPY app /RAG_app/app
COPY tests /RAG_app/tests

# expose port
EXPOSE 8000

# run the backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

### How to run ###
# Build docker image
# ``docker build -t rag-backend-server-img .``

# RUn docker container: --name <container name> <docker image name>
# ``docker run -d -p 8000:8000 --name rag-app-backend-container rag-app-backend-server-img``


