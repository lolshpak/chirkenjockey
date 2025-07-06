# Configuration file for the Student Office Support Chatbot

# Flask settings
FLASK_HOST = '127.0.0.1'
FLASK_PORT = 5000
DEBUG = True

# Ollama settings
OLLAMA_URL = 'http://localhost:11434'
MODEL_NAME = 'llama2'

# Chatbot settings
MAX_RESPONSE_LENGTH = 500
TEMPERATURE = 0.7
SYSTEM_PROMPT = """You are a helpful assistant for a student office. You help students with:
- Enrollment procedures
- Academic records and transcripts
- Financial aid and scholarships
- Campus services and facilities
- Academic policies and deadlines
- Course registration
- General administrative questions

Keep your responses helpful, concise, and friendly. If you don't know something specific, 
direct the student to contact the office directly."""

# Knowledge base file
KNOWLEDGE_BASE_FILE = 'data/student_office_knowledge.txt'