from flask import Flask, render_template, request, jsonify
from chatbot import StudentOfficeChatbot
import config

app = Flask(__name__)
chatbot = StudentOfficeChatbot()

@app.route('/')
def index():
    """Main page with chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        user_message = request.json.get('message', '')
        
        if not user_message.strip():
            return jsonify({'error': 'Empty message'}), 400
        
        # Get response from chatbot
        bot_response = chatbot.get_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({
            'error': 'Sorry, I encountered an error. Please try again.',
            'status': 'error'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model': config.MODEL_NAME,
        'ollama_url': config.OLLAMA_URL
    })

if __name__ == '__main__':
    print("Starting Student Office Support Chatbot...")
    print(f"Server will run on http://{config.FLASK_HOST}:{config.FLASK_PORT}")
    print("Make sure Ollama is running with llama2 model!")
    
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=config.DEBUG
    )