# Ollama Local Chat
A Flask app using local Ollama API.

# Requirements
```
pip install flask olama
```

# Local Network Use Case

## Windows
Install WSL  
```
wsl
```
Install Ubuntu via WSL  
```
wsl --install Ubuntu
```
Install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```
Run Ollama to obtain a Model
```
ollama run gemma3
```
Exit Interactive Chat
```
/bye
```
Export WSL
```
wsl --export Ubuntu <path>\Ubuntu.tar
```
On a Local Networked Windows Environment
```
wsl --import Ubuntu <path> <path>\Ubuntu.tar
```
Run WSL instance
```
wsl -d Ubuntu
```
Run Flask App from Windows or WSL instance
```
python app.py
```
Visit via Browser
```
127.0.0.1:5000
```
