from model import model
from langchain_core.messages import HumanMessage, SystemMessage


# 2. Funzione dell'agente
def run_local_agent(query):
    messages = [
        SystemMessage(content="Sei un assistente intelligente che risponde alle domande usando un modello locale."),
        HumanMessage(content=query)
    ]
    # Il comando invoke rimane identico! 
    # Questa è la forza di LangChain: cambi il "motore" ma il codice resta uguale.
    response = model.invoke(messages)
    return response.content

if __name__ == "__main__":
    test_query = "Riesci a rispondere a questa domanda usando il modello locale?"
    print("-" * 20)
    print(f"User: {test_query}")
    print("-" * 20)
    
    try:
        result = run_local_agent(test_query)
        print(f"Agent Locale: {result}")
    except Exception as e:
        print(f"Errore: Assicurati che Ollama sia avviato! \n{e}")
        
    print("-" * 20)