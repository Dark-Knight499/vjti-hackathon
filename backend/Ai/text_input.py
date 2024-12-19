import json
from utils.voice import say
from graph_state import State
def text_input(state: State) -> State:
    llm = state["llm"]
    action = state["action"]
    if action == "login":
        login_info = get_login_info()
        state["account_number"] = login_info.get("account_number")
        state["password"] = login_info.get("password")
    elif action == "otp":
        otp_info = get_otp()
        state["otp"] = otp_info.get("otp")
    elif action == "transfer":
        transfer_details = get_transfer_details()
        state["transfer_account_number"] = transfer_details.get("account_number")
        state["amount"] = transfer_details.get("amount")
    elif action == "card":
        card_details = get_card_details()
        state["card_number"] = card_details.get("card_number")
    else:
        state["error"] = "Invalid action"
    return state

def get_login_info() -> dict:
    say("Please enter your bank account number")
    account_number = input("Please enter your bank account number: ")
    say("Please enter your password")
    password = input("Please enter your password: ")
    print(account_number, password)

    response = json.loads(f'{{"account_number": "{account_number}", "password": "{password}"}}')
    return response

def get_otp() -> dict:
    say("Please enter the OTP sent to your phone")
    otp = input("Please enter the OTP sent to your phone: ")
    print(otp)
    
    response = json.loads(f'{{"otp": "{otp}"}}')
    return response

def get_transfer_details() -> dict:
    say("Please enter the account number of the person you want to transfer money to")
    account_number = input("Please enter the account number of the person you want to transfer money to: ")
    say("Please enter the amount you want to transfer")
    amount = input("Please enter the amount you want to transfer: ")
    print(account_number, amount)

    response = json.loads(f'{{"account_number": "{account_number}", "amount": "{amount}"}}')
    return response

def get_card_details() -> dict:
    say("Please enter your card number")
    card_number = input("Please enter your card number: ")
    print(card_number)
    
    response = json.loads(f'{{"card_number": "{card_number}"}}')
    return response

if __name__ == "__main__":
    state = {"action": "login"}
    login_info = text_input(state)
    print(login_info)
    state["action"] = "otp"
    otp_info = text_input(state)
    print(otp_info)
