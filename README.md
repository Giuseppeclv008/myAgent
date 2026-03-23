# Istruzioni Setup Progetto LangChain + Ollama

Before installing libraries it is recommended to open a virtual environment.

```
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows
```
You'll see (venv) in your terminal when active. Run ```deactivate``` to exit.

---


## 1. Libraries setup
Copy and paste this command 
```
pip install langchain langchain-ollama langchain-core 
langchain-community
```
## 2. Model Requirements (Ollama)
The code uses the 'llama3' template. Make sure you have it configured:

1. Download Ollama from https://ollama.com
2. In the terminal, run: ```ollama pull llama3```
3. Make sure the Ollama app is launched.

--- 

