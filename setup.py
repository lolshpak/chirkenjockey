#!/usr/bin/env python3
"""
Setup script for Student Office Support Chatbot
This script helps you set up the project and test connections.
"""

import os
import sys
import subprocess
import requests
from pathlib import Path

def check_python():
    """Check Python version"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Warning: Python 3.8 or higher is recommended")
        return False
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['templates', 'static', 'data']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Created directory: {directory}")

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("✓ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def test_ollama_connection():
    """Test connection to Ollama"""
    print("Testing Ollama connection...")
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print("✓ Ollama is running")
            print("Available models:")
            for model in models:
                print(f"  - {model['name']}")
            
            # Check if llama2 is available
            model_names = [model['name'] for model in models]
            if any('llama2' in name for name in model_names):
                print("✓ Llama2 model found")
                return True
            else:
                print("❌ Llama2 model not found. Run: ollama pull llama2")
                return False
        else:
            print(f"❌ Ollama responded with status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Make sure it's running on localhost:11434")
        return False
    except Exception as e:
        print(f"❌ Error testing Ollama: {e}")
        return False

def run_health_check():
    """Run a quick health check"""
    print("\n" + "="*50)
    print("HEALTH CHECK")
    print("="*50)
    
    checks = [
        ("Python version", check_python),
        ("Ollama connection", test_ollama_connection),
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        print(f"\nChecking {check_name}...")
        if not check_func():
            all_passed = False
    
    return all_passed

def main():
    """Main setup function"""
    print("Student Office Support Chatbot Setup")
    print("="*40)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed during package installation")
        return False
    
    # Run health check
    if run_health_check():
        print("\n✅ Setup completed successfully!")
        print("\nTo start the chatbot:")
        print("1. Make sure Ollama is running: ollama serve")
        print("2. Run the chatbot: py main.py")
        print("3. Open your browser to: http://localhost:5000")
        return True
    else:
        print("\n❌ Setup completed with issues. Please fix the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)