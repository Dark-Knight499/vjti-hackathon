from langgraph.graph import StateGraph, START, END
from graph_state import State
from tools import *
from graph_state import State
from utils.voice import say,listen
from langchain_core.messages import HumanMessage, AIMessage

def model(state: State) -> State:
    user_input = listen()
    print(f"User: {user_input}")
    state["messages"] = HumanMessage(content=user_input)
    response = state["llm"].invoke(state["messages"])
    state["messages"] = response
    say(response.content)  # Speaking the response
    return state

def router(state : State):
    if "bye" in State["messages"][-1].content:
        return "end"
    if State["messages"][-1].tool_calls == []:
        return "model"
    else:
        return State["messages"][-1].tool_calls[0].name

graph_builder = StateGraph(State)
graph_builder.add_node("initiate_get_balance", get_balance)
graph_builder.add_node("initiate_transfer", transfer)
graph_builder.add_node("initiate_get_transaction_details", get_transaction_details)
graph_builder.add_node("initiate_get_card_details", get_card_details)
graph_builder.add_node("initiate_get_full_account_details", get_full_account_details)
graph_builder.add_node("initiate_send_whatsapp", send_whatsapp)
graph_builder.add_node("model", model)


tool_nodes = {
    "initiate_balance_check": "initiate_get_balance",
    "initiate_transfer_of_funds": "initiate_transfer",
    "initiate_transaction_details_fetch": "initiate_get_transaction_details",
    "initiate_card_details_fetch": "initiate_get_card_details",
    "initiate_full_account_details_fetch": "initiate_get_full_account_details", 
    "initiate_whatsapp_message_send": "initiate_send_whatsapp",
    "model": "model"}
graph_builder.set_entry_point("model")
graph_builder.add_conditional_edges("model", router, tool_nodes)
graph_builder.add_edge("initiate_get_balance", "model")
graph_builder.add_edge("initiate_transfer", "model")
graph_builder.add_edge("initiate_get_transaction_details", "model")
graph_builder.add_edge("initiate_get_card_details", "model")
graph_builder.add_edge("initiate_get_full_account_details", "model")
graph_builder.add_edge("initiate_send_whatsapp", "model")

graph = graph_builder.compile()

with open("graph_output.png", "wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())


