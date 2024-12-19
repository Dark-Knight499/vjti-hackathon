# from tools import *
# from dotenv import load_dotenv
# from langchain_core.messages import HumanMessage, AIMessage
# llm_tools = [get_account_details, get_account_balance, get_transaction_details,get_card_details,get_full_account_details,send_whatsapp]
# from langchain_google_genai import ChatGoogleGenerativeAI
# from pprint import pprint
# def execute_tool_calls(tool_calls):
#     """Executes tool functions based on the provided tool calls.
#     Args:
#         tool_calls: List of tool call dictionaries.
#     Returns:
#         List of results from the executed tool functions.
#     """
#     if len(tool_calls) == 0:
#         return
#     results = []
#     for call in tool_calls:
#         tool_name = call['name']
#         args = call['args']
#         if tool_name in globals():
#             tool_function = globals()[tool_name]
#             result = tool_function.invoke({**args})
#             results.append({"The tool that was called": tool_name, "The result of the tool": result})

# llm = ChatGoogleGenerativeAI(model="gemini-pro",
#                               google_api_key=os.getenv("GOOGLE_API_KEY"))
# llm = llm.bind_tools(llm_tools)
# message = []
# while True:
#     message.append(HumanMessage(content = input("You: ")))
#     print(message)
#     response = llm.invoke(message)
#     print("\n\n\n")
#     print(response.content)
#     print(response.tool_calls)
#     print(execute_tool_calls(response.tool_calls))
#     print("\n\n\n")




from Ai.input_graph import graph
from graph_state import State
from typing import TypedDict
from langchain_google_genai import GoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
def login(state:State):
    state["action"] = "login"
    graph.invoke(state)
    return graph.get_state()
def otp(state:State):
    state["action"] = "otp"
    graph.invoke(state)
    return graph.get_state()
def transfer(state:State):
    state["action"] = "transfer"
    graph.invoke(state)
    return graph.get_state()
def card(state:State):
    state["action"] = "card"
    graph.invoke(state)
    return graph.get_state()


graph2 = StateGraph(State)
graph2.add_node("login", login)
graph2.add_node("card",card)
graph2.set_entry_point("login")
graph2.add_edge("login","card")
graph2.add_edge("card",END)

graph2 = graph2.compile()

input_data = {
    "llm": GoogleGenerativeAI(model="gemini"),
    "account_number": None,
    "password": None,
    "otp": None,
    "action": "login",
    "card_number": None,
    "messages": []
}

result = graph2.invoke(input_data)

# Print the result
print(result)
with open("graph_output.png", "wb") as f:
    f.write(graph2.get_graph().draw_mermaid_png())