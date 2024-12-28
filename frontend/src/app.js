const uploadButton = document.getElementById("uploadButton");
const fileInput = document.getElementById("fileInput");
const uploadStatus = document.getElementById("uploadStatus");
const sendButton = document.getElementById("sendButton");
const chatInput = document.getElementById("chatInput");
const chatBox = document.getElementById("chatBox");

const backendUrl = "http://127.0.0.1:8000"; // FastAPI backend URL
let session_id = null; // Session ID initialized on app load

// Initialize session by fetching session_id
async function initializeSession() {
    try {
        const response = await fetch(`${backendUrl}/start_session/`);
        const result = await response.json();
        if (response.ok && result.session_id) {
            session_id = result.session_id; // Store the session_id
            console.log("Session initialized with ID:", session_id);
        } else {
            console.error("Failed to initialize session. No session_id received.");
        }
    } catch (error) {
        console.error("Error initializing session:", error);
    }
}

// Call initializeSession on page load
window.onload = initializeSession;

// Handle File Upload
uploadButton.addEventListener("click", async () => {
    if (!session_id) {
        alert("Session not initialized. Please refresh the page.");
        return;
    }

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
            headers: { "session_id": session_id }, // Pass session_id in headers if needed
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
    const query = chatInput.value;

    if (!query) {
        alert("Please enter a query.");
        return;
    }

    if (!session_id) {
        alert("Session not initialized. Please refresh the page.");
        return;
    }

    try {
        const response = await fetch(`${backendUrl}/chat/`, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ session_id, query }),
        });
        const result = await response.json();
        if (response.ok) {
            const chatResponse = document.createElement("p");
            chatResponse.textContent = `Bot: ${result.response}`;
            chatBox.appendChild(chatResponse);
        } else {
            alert(result.detail);
        }
    } catch (error) {
        alert("An error occurred while processing your query.");
        console.error(error);
    }
});
