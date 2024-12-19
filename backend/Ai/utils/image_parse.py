from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv(r"C:\Harsh\vjti-hackathon\backend\Ai\.env")
import os
def image_parse(image_path:str)->str:
    parser = LlamaParse(
        verbose=False,
        result_type="markdown",
        premium_mode=True)
    parsed_doc = parser.load_data(r"C:\Harsh\vjti-hackathon\backend\Ai\captured_image.jpg")
    print(parsed_doc[0])
    return parsed_doc[0]
if __name__ == "__main__":
    filename = r"C:\Harsh\vjti-hackathon\captured_image.jpg"
    print(image_parse(filename))

