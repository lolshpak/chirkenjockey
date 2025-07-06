import requests
import json
import os
import config

class StudentOfficeChatbot:
    def __init__(self):
        self.ollama_url = config.OLLAMA_URL
        self.model_name = config.MODEL_NAME
        self.system_prompt = config.SYSTEM_PROMPT
        self.knowledge_base = self.load_knowledge_base()
        
    def load_knowledge_base(self):
        """Load knowledge base from file"""
        try:
            if os.path.exists(config.KNOWLEDGE_BASE_FILE):
                with open(config.KNOWLEDGE_BASE_FILE, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                return ""
        except Exception as e:
            print(f"Error loading knowledge base: {e}")
            return ""
    
    def get_response(self, user_message):
        """Get response from Ollama"""
        try:
            # Prepare the prompt with context
            full_prompt = f"{self.system_prompt}\n\n"
            
            if self.knowledge_base:
                full_prompt += f"Knowledge Base:\n{self.knowledge_base}\n\n"
            
            full_prompt += f"Student Question: {user_message}\n\nResponse:"
            
            # Prepare request to Ollama
            payload = {
                "model": self.model_name,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": config.TEMPERATURE,
                    "num_predict": config.MAX_RESPONSE_LENGTH
                }
            }
            
            # Make request to Ollama
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'Sorry, I could not generate a response.')
            else:
                return f"Error: Could not connect to Ollama (Status: {response.status_code})"
                
        except requests.exceptions.ConnectionError:
            return "Error: Could not connect to Ollama. Make sure Ollama is running on localhost:11434"
        except requests.exceptions.Timeout:
            return "Error: Request timed out. The model might be taking too long to respond."
        except Exception as e:
            print(f"Error in get_response: {e}")
            return "Sorry, I encountered an error while processing your request."
    
    def test_connection(self):
        """Test connection to Ollama"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                model_names = [model['name'] for model in models]
                return True, model_names
            else:
                return False, []
        except Exception as e:
            return False, str(e)