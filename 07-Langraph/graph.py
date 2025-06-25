from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
# Initialize OpenAI client
client = OpenAI()

class State(TypedDict):
    query: str
    llm_result: str | None
    

def chat_bot(state : State):
    query = state['query']
    #llm call
    llm_response=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ]
    )
    # result="How Can I help you?"
    state['llm_result'] = llm_response.choices[0].message.content
    return state

graph_builder=StateGraph(State)
graph_builder.add_node("chat_bot", chat_bot)
graph_builder.add_edge(START, "chat_bot")
graph_builder.add_edge("chat_bot", END)

graph= graph_builder.compile()

def main():
    user=input("Enter your query: ")
    
    #invoke the graph
    _state={
        "query": user,
        "llm_result": None
    }
    graph_result=graph.invoke(_state)
    print("graph_result",graph_result)
    

main()