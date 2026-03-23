from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
# 1. Configura il modello locale
# Assicurati che il nome 'llama3' corrisponda a quello scaricato con Ollama
model = ChatOllama(
    model="llama3",
    temperature=0.7,
    tools=["convert_temperature", "save_to_file", "read_from_file"]  # Specifica gli strumenti che l'agente può utilizzare
)

def run_local_agent(query):
    messages = [
        SystemMessage(content="""
                                You are a helpful local assistant that can convert temperatures between Celsius and Fahrenheit. 
                                Always use the convert_temperature tool when users ask for temperature conversions.
                                You can also save and read files using the save_to_file and read_from_file tools.
                                """),
        HumanMessage(content=query)
    ]
    # Il comando invoke rimane identico! 
    # Questa è la forza di LangChain: cambi il "motore" ma il codice resta uguale.
    response = model.invoke(messages)
    return response.content
