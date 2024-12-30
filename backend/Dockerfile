# from base package
FROM python:3.10-slim

# Set environment variables
# Ensure Python output is logged immediately
ENV PYTHONUNBUFFERED=1  
# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1  

# Set working dir inside the container
WORKDIR /backend

# install dependencies
COPY requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r /backend/requirements.txt
# Download the SpaCy model
RUN python -m spacy download en_core_web_sm

# Copy backend files to the container working dir
COPY app /backend/app
COPY tests /backend/tests

# expose port
EXPOSE 8000

# run the backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

### How to run ###
# Build docker image
# ``docker build -t rag-backend-server-img .``

# RUn docker container: --name <container name> <docker image name>
# ``docker run -d -p 8000:8000 --name rag-app-backend-container rag-app-backend-server-img``


