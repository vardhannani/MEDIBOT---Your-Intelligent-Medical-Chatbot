function addMessage(content, sender) {
    const message = document.createElement("div");
    message.classList.add("message", sender);
    message.textContent = content;
    const chatMessages = document.getElementById("chat-messages");
    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();

    if (message) {
        addMessage(message, "user");
        userInput.value = "";

        fetch("/get_response", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, "bot");
        });
    }
}