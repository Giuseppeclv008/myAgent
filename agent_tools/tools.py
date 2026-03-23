import os
from langchain.tools import tool
from langchain_core.messages import HumanMessage

@tool
def save_to_file(content: str, filename: str) -> str:
    """Salva il contenuto in un file specificato."""
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"File '{filename}' salvato con successo."
    except Exception as e:
        return f"Errore durante il salvataggio del file: {e}"
    
@tool
def read_from_file(filename: str) -> str:
    """Legge il contenuto da un file specificato."""
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Errore durante la lettura del file: {e}"

@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature between Celsius and Fahrenheit.
    
    Args:
        value: The temperature value to convert
        from_unit: Source unit ("celsius" or "fahrenheit")
        to_unit: Target unit ("celsius" or "fahrenheit")
    
    Returns:
        Converted temperature value
    """
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return (value - 32) * 5/9
    elif from_unit.lower() == to_unit.lower():
        return value
    else:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")