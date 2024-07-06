import os 
from typing import TextIO

def load_text_file(filename: str) -> TextIO:
    """
    Reads the contents of a text file from the specified full path.
    
    Args:
        filename (str): The full path of the text file to read.
        
    Returns:
        Any: The contents of the text file, stripped of newline characters.
        
    """

    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {filename} does not exist.")

