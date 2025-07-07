@echo off
echo Starting Student Office Support Chatbot...
echo.

echo Checking if Ollama is running...
curl -s http://localhost:11434/api/tags >nul 2>&1
if %errorlevel% neq 0 (
    echo Ollama is not running. Please start it first:
    echo   ollama serve
    echo.
    pause
    exit /b 1
)

echo Ollama is running!
echo.

echo Starting chatbot server...
py main.py

pause