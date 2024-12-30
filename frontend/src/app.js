const uploadButton = document.getElementById("uploadButton");
const fileInput = document.getElementById("fileInput");
const uploadStatus = document.getElementById("uploadStatus");
const sendButton = document.getElementById("sendButton");
const chatInput = document.getElementById("chatInput");
const chatBox = document.getElementById("chatBox");

const backendUrl = "http://127.0.0.1:8000"; // FastAPI backend URL // for locally run: "http://127.0.0.1:8000"; for docker run: "http://backend:8000"
let session_id = null; // Session ID initialized on app load


async function initializeSession() {
    try {
        const response = await fetch(`${backendUrl}/start_session/`);
        const result = await response.json();
        console.log(result);

        if (result.session_id) {
            session_id = result.session_id; // Store session_id for later use
            console.log("Session ID initialized:", session_id);
        } else {
            console.error("Failed to initialize session. No session_id received.");
            alert("Failed to initialize session. Please try reloading the page.");
        }
    } catch (error) {
        console.error("Error initializing session:", error);
        alert("Error initializing session. Please check the backend or reload the page.");
    }
}

// Call initializeSession when the page loads
window.onload = initializeSession;

// Handle File Upload
uploadButton.addEventListener("click", async () => {
    const file = fileInput.files[0];
    if (!file) {
        uploadStatus.textContent = "Please select a file to upload.";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch(`${backendUrl}/upload/`, {
            method: "POST",
            body: formData,
        });
        const result = await response.json();
        if (response.ok) {
            uploadStatus.textContent = result.message;
        } else {
            uploadStatus.textContent = result.detail;
        }
    } catch (error) {
        uploadStatus.textContent = "An error occurred while uploading the file.";
        console.error(error);
    }
});

// Handle Chat Queries
sendButton.addEventListener("click", async () => {
    console.log("Backend URL:", backendUrl);
    const query = chatInput.value.trim();

    if (!query) {
        alert("Please enter a query.");
        return;
    }

    if (!session_id) {
        alert("Session not initialized. Please refresh the page.");
        console.error("Session ID is null.");
        return;
    }

    try {

        console.log("Session ID:", session_id);
        console.log("Making request to /chat/ endpoint with query:", query);

        const formData = new URLSearchParams(); // Properly encode the form data
        formData.append("query", query);
        formData.append("user_id", session_id);

        const response = await fetch(`${backendUrl}/chat/`, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData,
        });

        const result = await response.json();
        if (response.ok) {
            const chatResponse = document.createElement("p");
            chatResponse.textContent = `Bot: ${result.response}`;
            chatBox.appendChild(chatResponse);
        } else {
            alert(result.detail || "Failed to process query.");
        }
    } catch (error) {
        alert("An error occurred while processing your query.");
        console.error(error);
    }
});
