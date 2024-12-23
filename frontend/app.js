const uploadButton = document.getElementById("uploadButton");
const fileInput = document.getElementById("fileInput");
const uploadStatus = document.getElementById("uploadStatus");
const sendButton = document.getElementById("sendButton");
const chatInput = document.getElementById("chatInput");
const chatBox = document.getElementById("chatBox");

const backendUrl = "http://127.0.0.1:8000"; // FastAPI backend URL

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
    const query = chatInput.value;
    if (!query) {
        alert("Please enter a query.");
        return;
    }

    try {
        const response = await fetch(`${backendUrl}/chat/`, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ query }),
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
