from utils import bank
from graph_state import State
from langchain_core.messages import AIMessage
from input_graph import input_graph
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def get_balance(state: State) -> State:
    balance = bank.get_balance(state["account_number"])
    state["messages"] = [AIMessage(balance)]
    return state

def transfer(state: State) -> State:
    state["action"] = "transfer"
    state = dict(input_graph.invoke(state))
    transfer_status = bank.transfer(state["account_number"], state["transfer_account_number"], state["amount"])
    state["messages"] = [AIMessage(transfer_status)]
    return state

def get_transaction_details(state: State) -> State:
    transaction_details = bank.get_transaction_details(state["account_number"])
    state["messages"] = [AIMessage(transaction_details)]
    return state


def get_card_details(state: State) -> State:
    card_details = bank.get_card_details(state["account_number"], state["card_number"])
    state["messages"] = [AIMessage(card_details)]
    return state


def get_full_account_details(state: State) -> State:
    full_account_details = bank.get_full_account_details(state["account_number"])
    state["messages"] = [AIMessage(full_account_details)]
    return state

def send_whatsapp(state: State) -> State:
    status = bank.send_whatsapp()
    state["messages"] = [AIMessage(status)]

    return state


if __name__ == "__main__":
    input_data = {
    "llm": GoogleGenerativeAI(model="gemini"),
    "account_number": 4567890123456789,
    "transfer_account_number": None,
    "amount": None,
    "password": None,
    "otp": None,
    "action": "login",
    "card_number": None,
    "messages": []
}
    result = transfer(input_data)
    print(result)