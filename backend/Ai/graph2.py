from tools import *
llm_tools = [get_account_details, get_account_balance, get_transaction_details,get_card_details,get_full_account_details,send_whatsapp]
from typing import Annotated
from typing_extensions import TypedDict,Union,Literal
from langchain_google_genai import GoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from utils.voice import say,listen