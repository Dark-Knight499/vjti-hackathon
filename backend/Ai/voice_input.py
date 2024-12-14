from utils.voice import listen , say
from prompts.voice_prompts import parse_bank_details_prompt, parse_otp_prompt
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import GoogleGenerativeAI

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

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    llm = GoogleGenerativeAI(model ="gemini-1.5-pro")
    login_info = get_login_info(llm)
    otp_info = get_otp(llm)
    print(login_info)
    print(otp_info)
    say("Thank you for your input")


