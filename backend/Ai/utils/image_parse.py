from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv("Ai/.env")
import os
def image_parse(image_path:str)->str:
    parser = LlamaParse(
        premium_mode=True)
    parsed_doc = parser.load_data(image_path)
    return parsed_doc[0]
if __name__ == "__main__":
    print(image_parse(r"C:\Users\jaind\Downloads\img.jpg"))

