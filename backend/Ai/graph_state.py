from typing_extensions import TypedDict,Union,Literal
from typing import Annotated
from langchain_google_genai import GoogleGenerativeAI
from langgraph.graph.message import add_messages

class State(TypedDict):
    llm: GoogleGenerativeAI
    account_number: str | None
    transfer_account_number: str | None
    amount: float | None
    password: str | None
    otp: str | None
    action: Union[Literal["login"], Literal["otp"], Literal["transfer"], Literal["card"]]
    card_number: str | None
    messages: Annotated[list, add_messages]
    error : str | None