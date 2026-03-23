from langchain_ollama import ChatOllama
# 1. Configura il modello locale
# Assicurati che il nome 'llama3' corrisponda a quello scaricato con Ollama
model = ChatOllama(
    model="llama3",
    temperature=0.7,
)
