# Setup base package
FROM python:3.10-slim

# Set working dir inside the container
WORKDIR /app/frontend

# Copy frontend files to the working idr
COPY frontend/src /frontend

# Expose the port on which the HTTP server will run
EXPOSE 8080

# Run python http server
CMD ["python", "-m", "http.server", "8080"]

### How to run ###
# Build docker image
# ``docker build -t rag-frontend-server-img``

# RUn docker container: --name <container name> <docker image name>
# ``docker run -d -p 8080:8080 --name rag-app-fronetend-server-cont rag-app-frontend-server-img``

