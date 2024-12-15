from utils.voice import listen , say
from prompts.voice_prompts import (parse_bank_details_prompt, 
                                   parse_otp_prompt, 
                                   parse_transfer_details_prompt,
                                   parse_card_details_prompt)
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import GoogleGenerativeAI


def voice_input(state: dict):
    llm = state["llm"]
    action = state["action"]
    if action == "login":
        return get_login_info(llm)
    elif action == "otp":
        return get_otp(llm)
    elif action == "transfer":
        return get_transfer_details(llm)
    elif action == "card":
        return get_card_details(llm)
    else:
        return "Invalid action"
    

#hande puncuation and face value of puncuation after words
def get_login_info(llm : GoogleGenerativeAI)->str:
    say("Please say your bank account number")
    account_number = listen()
    say("Please say your password")
    password = listen()
    print(account_number, password)

    prompt_template = PromptTemplate(template=parse_bank_details_prompt, input_variables=["account_number", "password"])
    prompt = prompt_template.format(account_number=account_number, password=password)
    
    parser = JsonOutputParser()
    login_info = parser.invoke(llm.invoke(prompt))
    return login_info

def get_otp(llm: GoogleGenerativeAI) -> str:
    say("Please say the OTP sent to your phone")
    otp = listen()
    print(otp)
    
    prompt_template = PromptTemplate(template=parse_otp_prompt, input_variables=["otp"])
    prompt = prompt_template.format(otp=otp)
    parser = JsonOutputParser()

    otp_info = parser.invoke(llm.invoke(prompt))
    return otp_info


#write a function to get transfer of money details
def get_transfer_details(llm: GoogleGenerativeAI)->str:
    say("Please say the account number of the person you want to transfer money to")
    account_number = listen()
    say("Please say the amount you want to transfer")
    amount = listen()
    print(account_number, amount)

    prompt_template = PromptTemplate(template=parse_transfer_details_prompt, input_variables=["account_number", "amount"])
    prompt = prompt_template.format(account_number=account_number, amount=amount)
    
    parser = JsonOutputParser()
    transfer_details = parser.invoke(llm.invoke(prompt))
    return transfer_details



#write a function to card details to be blocked
def get_card_details(llm: GoogleGenerativeAI)->str:
    say("Please say your card number")
    card_number = listen()
    print(card_number)
    
    prompt_template = PromptTemplate(template=parse_card_details_prompt, input_variables=["card_number"])
    prompt = prompt_template.format(card_number=card_number)
    
    parser = JsonOutputParser()
    card_details = parser.invoke(llm.invoke(prompt))
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




