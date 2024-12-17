from typing import Annotated
from typing_extensions import TypedDict,Union,Literal
from langchain_google_genai import GoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from utils.voice import say,listen
from voice_input import voice_input
from text_input import text_input
from vision_input import vision_input
class State(TypedDict):
    llm: GoogleGenerativeAI
    account_number: str | None
    password: str | None
    otp: str | None
    action: Union[Literal["login"], Literal["otp"], Literal["transfer"], Literal["card"]]
    card_number: str | None
    messages: Annotated[list, add_messages]

def __init__ (state: State) -> State:
    state["llm"] = GoogleGenerativeAI(model="gemini-pro")
    return state

def choose(state: State) -> str:
    say("By which method would you like to login? Text or Voice or Camera")
    method = listen()
    if "text" in method:
        state["action"] = "login"
        return "text"
    elif "voice" in method:
        state["action"] = "login"
        return "voice"
    elif "camera" in method:
        state["action"] = "login"
        return "camera"

def you_have_made_it(state: State) -> str:
    say("You have successfully made it to the end")
    
graph_builder = StateGraph(State)
graph_builder.add_node("__init__", __init__)
graph_builder.add_node("voice_input", voice_input)
graph_builder.add_node("text_input", text_input)
graph_builder.add_node("vision_input", vision_input)

# Set the entry point to START
graph_builder.set_entry_point("__init__")

# Define edges
graph_builder.add_conditional_edges("__init__", choose, {
    "text": "text_input",
    "voice": "voice_input",
    "camera": "vision_input"
})

# Connect input nodes to END
graph_builder.add_edge("text_input", END)
graph_builder.add_edge("voice_input", END)
graph_builder.add_edge("vision_input", END)

# Compile the graph
graph = graph_builder.compile()


def initialize_state(state: State) -> State:
    state["llm"] = GoogleGenerativeAI(model="gemini-pro")
    return state

graph_builder = StateGraph(State)
graph_builder.add_node("initialize_state", initialize_state)
graph_builder.add_node("voice_input", voice_input)
graph_builder.add_node("text_input", text_input)
graph_builder.add_node("vision_input", vision_input)

# Set the entry point to START
graph_builder.set_entry_point("initialize_state")

# Define edges
graph_builder.add_conditional_edges("initialize_state", choose, {
    "text": "text_input",
    "voice": "voice_input",
    "camera": "vision_input"
})

# Connect input nodes to END
graph_builder.add_edge("text_input", END)
graph_builder.add_edge("voice_input", END)
graph_builder.add_edge("vision_input", END)

# Compile the graph
graph = graph_builder.compile()
input_data = {
    "llm": GoogleGenerativeAI(model="gemini"),
    "account_number": None,
    "password": None,
    "otp": None,
    "action": "login",
    "card_number": None,
    "messages": []
}

# Invoke the graph
result = graph.get_prompts()

# Print the result
print(result)




