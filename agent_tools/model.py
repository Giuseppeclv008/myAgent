from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from tools import save_to_file, read_from_file, convert_temperature

# 1. Configura il modello locale
# Assicurati che il nome 'llama3' corrisponda a quello scaricato con Ollama
llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0.7,
)

tools = [save_to_file, read_from_file, convert_temperature]
model = llm.bind_tools(tools)

def run_local_agent(query):
    # if we don't specify to the agent that he can use a tool the agent will not be able to use it, so we need to specify it in the system message
    messages = [
        SystemMessage(content="""
                                You are a helpful local assistant.
                                You can convert temperatures and also save and read files.
                                Use the 'convert_temperature' tool for temperature conversions. 
                                Use the 'save_to_file' and 'read_from_file' tools for file operations.
                                """),
        HumanMessage(content=query)
    ]

    while True:
        response = model.invoke(messages)

        if not response.tool_calls:
            return response.content
        
        messages.append(response)

        for tool_call in response.tool_calls:
            if tool_call["name"] == "save_to_file":
                args = tool_call["args"]
                tool_output = save_to_file.invoke(args)
            elif tool_call["name"] == "read_from_file":
                args = tool_call["args"]
                tool_output = read_from_file.invoke(args)
            elif tool_call["name"] == "convert_temperature":
                args = tool_call["args"]
                tool_output = convert_temperature.invoke(args)
            else:
                tool_output = f"Error: Tool '{tool_call['name']}' not found."
            
            messages.append(ToolMessage(content=str(tool_output), tool_call_id=tool_call["id"]))
