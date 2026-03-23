from model import model, run_local_agent
from tools import *  # Importa tutti gli strumenti definiti in tools.py



if __name__ == "__main__":
    test_query = "Convert 25 degrees Celsius to Fahrenheit"
    print("-" * 20)
    print(f"User: {test_query}")
    print("-" * 20)
    
    try:
        result = run_local_agent(test_query)
        print(f"Agent Locale: {result}")
    except Exception as e:
        print(f"Errore: Assicurati che Ollama sia avviato! \n{e}")
        
    print("-" * 20)