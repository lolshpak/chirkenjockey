# AI-Powered Student Office Support Chatbot

A simple chatbot built with Python, Flask, and Ollama (Llama2) to help students with common office-related questions and procedures.

## Features

- Web-based chat interface
- Integration with Ollama (Llama2) for natural language processing
- Predefined knowledge base for student office procedures
- Simple and clean UI
- Easy to extend and customize

## Prerequisites

- Python 3.8 or higher
- Ollama installed with Llama2 model
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lolshpak/chirkenjockey.git
cd chirkenjockey
```

2. Install required packages:
```bash
py -m pip install -r requirements.txt
```

3. Make sure Ollama is running with Llama2:
```bash
ollama serve
ollama run llama2
```

## Usage

1. Run the application:
```bash
py main.py
```

2. Open your browser and go to `http://localhost:5000`

3. Start chatting with the bot about student office procedures!

## Configuration

Edit `config.py` to modify:
- Server port
- Ollama model settings
- Response parameters

## Adding Knowledge

Add common student office procedures and information to `data/student_office_knowledge.txt` to improve the chatbot's responses.

## Project Structure

- `main.py` - Flask web application entry point
- `chatbot.py` - Core chatbot logic and Ollama integration
- `templates/index.html` - Web interface
- `static/` - CSS and JavaScript files
- `data/` - Knowledge base files
- `config.py` - Configuration settings

## Contributing

This is a practice project. Feel free to fork and experiment!

## License

MIT License - feel free to use for learning purposes.