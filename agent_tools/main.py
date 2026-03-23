from model import model, run_local_agent
from tools import *  # Importa tutti gli strumenti definiti in tools.py



if __name__ == "__main__":
    
    test_query1 = "Convert 25 degrees Celsius to Fahrenheit"
    test_query2 = "What is 77 degrees Fahrenheit in Celsius?"
    test_query3 = "If it's 20°C outside, what would that be in Fahrenheit? Is that warm or cold?"
    test_query4 = """Save the text 'Hello, World!' to a file named 'greeting.txt'. 
                        Make sure to confirm that the file was saved successfully. 
                        In the previous query you said that the file was saved successfully, now read the content of 'greeting.txt' and tell me what it says.
                        Tell me where the file is located on my computer.
                """

    
    try:
        # # test1 simple conversion
        print(f"User: {test_query1}")
        print("-" * 20)
        result = run_local_agent(test_query1)
        print(f"Agent Locale: {result}")
        print("-" * 20)
    
        # # test2 Reverse conversion
        # result = run_local_agent(test_query2)
        # print(f"Agent Locale: {result}")
        # print("-" * 20)
        # print(f"User: {test_query2}")
        # print("-" * 20)
        
        # # test3 conversion with context, more complex query
        # result = run_local_agent(test_query3)
        # print(f"Agent Locale: {result}")
        # print("-" * 20)
        # print(f"User: {test_query3}")
        # print("-" * 20)
        
        # test4 file saving
        result = run_local_agent(test_query4)
        print("-" * 20)
        print(f"User: {test_query4}")
        print("-" * 20)
        print(f"Agent Locale: {result}")
    
        
    except Exception as e:
        print(f"Errore: Assicurati che Ollama sia avviato! \n{e}")
        
    print("-" * 20)