from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END 
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
from typing import Literal
from openai import OpenAI
# Initialize OpenAI client
client = OpenAI()

class ClassifyMessageResponse(BaseModel):
    isCodingQuestion: bool

class CodeAccuracyResponse(BaseModel):
    accuracy_percentage: str


class State(TypedDict):
    user_query: str
    llm_result: str | None
    accuracy_percentage: str | None
    isCodingQuestion: bool | None
    
def classify_query(state: State):
    query = state['user_query']
    SYSTEM_PROMPT="""
    You are an Ai Assistant and your job is to classify whether the user query is related to coding or not.
    Return the reposnse in specified  JSON boolean only.
    """
    
    #Structured Responses 
    # Here we will use pydantic or similar libraries to define structured responses.
    # LLM call for classification
    llm_response = client.beta.chat.completions.parse(
        model="gpt-4.1-nano",
        response_format=ClassifyMessageResponse,    
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ]
    )
    isCodingQuestion=llm_response.choices[0].message.parsed.isCodingQuestion
    state['isCodingQuestion'] = isCodingQuestion
    return state

# When we add conditional edges then we also need to specify the Literal type for the return value of the function.
def route_query(state: State)->Literal["general_query", "coding_query"]:
    is_coding= state['isCodingQuestion']
    if is_coding:
        return "coding_query"
    
    return "general_query"
    

def general_query(state:State):
    user_query= state['user_query']
    response= client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
    )
    state['llm_result'] = response.choices[0].message.content
    return state

def coding_query(state:State):
    user_query= state['user_query']
    SYSTEM_PROPMT="""You are an AI assistant specialized in coding queries. 
    Your task is to provide accurate and helpful responses to coding-related questions.
    """
    response= client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROPMT},
            {"role": "user", "content": user_query}
        ]
    )
    state['llm_result'] = response.choices[0].message.content
    return state

def coding_validate_query(state:State):
    user_query=state["user_query"]
    llm_code= state["llm_result"]
    SYSTEM_PROMPT=f"""You are an AI assistant specialized in validating coding queries.
    Your task is to provide accurate and helpful responses to coding-related questions.
    Just analyze the code and return the accuracy percentage of the code.
    Below is the user query and the code provided by the AI assistant.
    User Query: {user_query}
    Code: {llm_code}
    """
    
    llm_response = client.beta.chat.completions.parse(
        model="gpt-4.1",
        response_format=CodeAccuracyResponse,    
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ]
    )
    
    state['accuracy_percentage'] = llm_response.choices[0].message.parsed.accuracy_percentage
    return state

def reRoute_query(state: State) -> Literal["coding_query", END]:
    accuracy= state['accuracy_percentage']
    if accuracy and int(accuracy.strip('%')) >= 95:
        return END
    return "coding_query"


#Defining Nodes
graph_builder=StateGraph(State)
graph_builder.add_node("classify_query", classify_query)
graph_builder.add_node("route_query", route_query)
graph_builder.add_node("general_query", general_query)
graph_builder.add_node("coding_query", coding_query)
graph_builder.add_node("coding_validate_query", coding_validate_query)
graph_builder.add_node("reRoute_query", reRoute_query)

#Defining Edges
graph_builder.add_edge(START, "classify_query")
graph_builder.add_conditional_edges("classify_query",route_query)
graph_builder.add_edge("general_query", END)
graph_builder.add_edge("coding_query", "coding_validate_query")
graph_builder.add_conditional_edges("coding_validate_query", reRoute_query)
graph_builder.add_edge("reRoute_query", "coding_query")
graph_builder.add_edge("reRoute_query", END)


#compiling the graph
graph= graph_builder.compile()

def main():
    user_query=input("Enter your query: ")
    
    #invoke the graph
    _state:State={
        "user_query": user_query,
        "llm_result": None,
        "accuracy_percentage": None,
        "isCodingQuestion": None
    }
    #here we are invoking the graph to get the result directly
    # graph_result=graph.invoke(_state)
    # print("Graph Result:", graph_result)
    
    # we can also stream the result of the graph and display it to enhance the user experience
    for event in graph.stream(_state):
        print("Event:->",event)
    
main()