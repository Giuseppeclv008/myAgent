from model import model, run_local_agent
from tools import *  # Importa tutti gli strumenti definiti in tools.py



if __name__ == "__main__":
    
    test_query1 = "Convert 25 degrees Celsius to Fahrenheit"
    print("-" * 20)
    print(f"User: {test_query1}")
    print("-" * 20)
    
    test_query2 = "What is 77 degrees Fahrenheit in Celsius?"
    print("-" * 20)
    print(f"User: {test_query2}")
    print("-" * 20)
    
    test_query3 = "If it's 20°C outside, what would that be in Fahrenheit? Is that warm or cold?"
    print("-" * 20)
    print(f"User: {test_query3}")
    print("-" * 20)
    
    test_query4 = "Save the text 'Hello, World!' to a file named 'greeting.txt'."
    print("-" * 20)
    print(f"User: {test_query4}")
    print("-" * 20)
    
    
    try:
        # test1 simple conversion
        result = run_local_agent(test_query1)
        print(f"Agent Locale: {result}")
        
        # test2 Reverse conversion
        result = run_local_agent(test_query2)
        print(f"Agent Locale: {result}")
        
        # test3 conversion with context, more complex query
        result = run_local_agent(test_query3)
        print(f"Agent Locale: {result}")
        
        # test4 file saving
        result = run_local_agent(test_query4)
        print(f"Agent Locale: {result}")
        
    except Exception as e:
        print(f"Errore: Assicurati che Ollama sia avviato! \n{e}")
        
    print("-" * 20)