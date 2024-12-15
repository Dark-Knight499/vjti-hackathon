from utils.voice import say
from utils.vision import CameraCapture
from utils.image_parse import image_parse
from langchain.prompts import PromptTemplate
from prompts.vision_prompts import (
    parse_bank_details_prompt,
    parse_otp_prompt,
    parse_transfer_details_prompt,
    parse_card_details_prompt
)
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import GoogleGenerativeAI
import asyncio
import json

def get_login_info(llm) -> dict:
    say("Please take a picture of your bank account number and password")
    asyncio.run(CameraCapture().capture_image())
    filename = r"C:\Harsh\vjti-hackathon\backend\captured_image.jpg"
    text = image_parse(filename)
    print(text)
    
    prompt_template = PromptTemplate(template=parse_bank_details_prompt, input_variables=["text"])
    prompt = prompt_template.format(text=text)
    
    parser = JsonOutputParser()
    login_info = parser.invoke(llm.invoke(prompt))
    print(login_info)
    return login_info

def get_otp(llm) -> dict:
    say("Please take a picture of the OTP sent to your phone")
    asyncio.run(CameraCapture().capture_image())
    filename = r"C:\Harsh\vjti-hackathon\backend\captured_image.jpg"
    text = image_parse(filename)
    print(text)
    
    prompt_template = PromptTemplate(template=parse_otp_prompt, input_variables=["text"])
    prompt = prompt_template.format(text=text)
    
    parser = JsonOutputParser()
    otp_info = parser.invoke(llm.invoke(prompt))
    print(otp_info)
    return otp_info

def get_transfer_details(llm) -> dict:
    say("Please take a picture of the account number and amount you want to transfer")
    asyncio.run(CameraCapture().capture_image())
    filename = r"C:\Harsh\vjti-hackathon\backend\captured_image.jpg"
    text = image_parse(filename)
    print(text)
    
    prompt_template = PromptTemplate(template=parse_transfer_details_prompt, input_variables=["text"])
    prompt = prompt_template.format(text=text)
    
    parser = JsonOutputParser()
    transfer_details = parser.invoke(llm.invoke(prompt))
    print(transfer_details)
    return transfer_details

def get_card_details(llm) -> dict:
    say("Please take a picture of your card number")
    asyncio.run(CameraCapture().capture_image())
    filename = r"C:\Harsh\vjti-hackathon\backend\captured_image.jpg"
    text = image_parse(filename)
    print(text)
    
    prompt_template = PromptTemplate(template=parse_card_details_prompt, input_variables=["text"])
    prompt = prompt_template.format(text=text)
    
    parser = JsonOutputParser()
    card_details = parser.invoke(llm.invoke(prompt))
    print(card_details)
    return card_details

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    llm = GoogleGenerativeAI(model ="gemini-1.5-pro")
    login_info = get_login_info(llm)
    otp_info = get_otp(llm)
    print(login_info)
    print(otp_info)
    say("Thank you for your input")