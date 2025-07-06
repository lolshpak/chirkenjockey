// Main JavaScript for the chatbot interface
document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const chatMessages = document.getElementById('chatMessages');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const welcomeTime = document.getElementById('welcomeTime');
    
    // Set welcome message time
    welcomeTime.textContent = getCurrentTime();
    
    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // Auto-resize input as user types
    messageInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
    
    function sendMessage() {
        const message = messageInput.value.trim();
        
        if (!message) {
            return;
        }
        
        // Disable input while processing
        setInputState(false);
        
        // Add user message to chat
        addMessage(message, 'user');
        
        // Clear input
        messageInput.value = '';
        messageInput.style.height = 'auto';
        
        // Show loading indicator
        showLoading(true);
        
        // Send message to server
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            hideLoading();
            
            if (data.status === 'success') {
                addMessage(data.response, 'bot');
            } else {
                addMessage(data.error || 'Sorry, something went wrong. Please try again.', 'bot');
            }
        })
        .catch(error => {
            hideLoading();
            console.error('Error:', error);
            addMessage('Sorry, I couldn\'t connect to the server. Please check your connection and try again.', 'bot');
        })
        .finally(() => {
            setInputState(true);
            messageInput.focus();
        });
    }
    
    function addMessage(content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        if (type === 'user') {
            messageContent.innerHTML = `<strong>You:</strong> ${escapeHtml(content)}`;
        } else {
            messageContent.innerHTML = `<strong>Bot:</strong> ${escapeHtml(content)}`;
        }
        
        const messageTime = document.createElement('div');
        messageTime.className = 'message-time';
        messageTime.textContent = getCurrentTime();
        
        messageDiv.appendChild(messageContent);
        messageDiv.appendChild(messageTime);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function setInputState(enabled) {
        messageInput.disabled = !enabled;
        sendButton.disabled = !enabled;
        
        if (enabled) {
            sendButton.textContent = 'Send';
        } else {
            sendButton.textContent = 'Sending...';
        }
    }
    
    function showLoading(show) {
        if (show) {
            loadingIndicator.style.display = 'flex';
        } else {
            loadingIndicator.style.display = 'none';
        }
    }
    
    function hideLoading() {
        loadingIndicator.style.display = 'none';
    }
    
    function getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString('en-US', { 
            hour: '2-digit', 
            minute: '2-digit',
            hour12: true 
        });
    }
    
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;")
            .replace(/\n/g, "<br>");
    }
    
    // Focus on input when page loads
    messageInput.focus();
    
    // Add some example questions for testing
    const exampleQuestions = [
        "How do I register for classes?",
        "What documents do I need for enrollment?",
        "How can I get a transcript?",
        "What financial aid options are available?",
        "How do I drop a class?",
        "What are the academic deadlines?",
        "How do I change my major?",
        "What campus services are available?"
    ];
    
    // Add a helper function to show example questions (you can call this from console)
    window.showExampleQuestions = function() {
        console.log("Example questions you can try:");
        exampleQuestions.forEach((q, i) => {
            console.log(`${i + 1}. ${q}`);
        });
    };
    
    // Show example questions in console
    setTimeout(() => {
        console.log("💡 Student Office Chatbot loaded successfully!");
        console.log("Try typing one of these example questions:");
        exampleQuestions.slice(0, 3).forEach(q => console.log(`• ${q}`));
        console.log("Or call showExampleQuestions() to see all examples.");
    }, 1000);
});