from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()  # Load .env file
import os
import json
from datetime import datetime
import requests
import subprocess

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

def get_weather(city:str):
    url=f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong while fetching the weather data."

    

def run_command(command: str):
    result=os.system(command)
    return result;


def convert_to_fahrenheit(celsius_str: str) -> str:
    try:
        celsius = float(celsius_str)
        fahrenheit = (celsius * 9 / 5) + 32
        return f"{fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid input. Please provide a valid number."



def create_vite_project(project_name: str):
    try:
        subprocess.run(f"npm create vite@latest {project_name} -- --template react", check=True, shell=True)
        subprocess.run("npm install", cwd=project_name, check=True, shell=True)
        return f"✅ React + Vite project '{project_name}' created successfully!"
    except subprocess.CalledProcessError as e:
        return f"❌ Error creating project: {str(e)}"

available_tools={
    "get_weather": get_weather,
    "run_command": run_command,
    "convert_to_fahrenheit": convert_to_fahrenheit,
    "create_vite_project": create_vite_project   
}

SYSTEM_PROMPT = f"""
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You work on start, plan, action, observe mode.

    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.

    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    Output JSON Format:
    {{
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    Available Tools:
    - "get_weather": Takes a city name as an input and returns the current weather for the city
    - "run_command": Takes linux command as a string and executes the command and returns the output after executing it.
    - "convert_to_fahrenheit": Takes a temperature in Celsius as a float and returns the temperature in Fahrenheit as a string.
    - "create_vite_project": Takes a project name as a string and creates a React + Vite project with the given name.
    

    Example:
    User Query: What is the weather of new york?
    Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york" }}
    Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
    Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
    Output: {{ "step": "observe", "output": "12 Degree Cel" }}
    Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}

"""

client =OpenAI(
    base_url=endpoint,
    api_key=token,
)
messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
]

while True:
    user_input=input("Enter the user query: ")
    messages.append({"role": "user", "content": user_input})
    while True:
        response=client.chat.completions.create(
            messages=messages,
            model=model,
            response_format={
                "type": "json_object",
            }
        )
        #dumps used to convert the python object to json string
        #loads used to convert the json string to python dictionary
        messages.append({"role": "assistant", "content":str(response.choices[0].message.content)})
        # print("🤖:-> ", response.choices[0].message.content)
        parsed_response=json.loads(response.choices[0].message.content)
        if parsed_response.get("step")=="plan":
            print(f"🤖:-> {parsed_response.get('content')}")
            continue
        
        if parsed_response.get("step")=="action":
            tool_name=parsed_response.get("function")
            tool_input=parsed_response.get("input")
            
            print(f"🤖:-> Performing action with tool: {tool_name} and input: {tool_input}")
            
            if available_tools.get(tool_name) != False:
                output=available_tools[tool_name](tool_input)
                messages.append({"role": "assistant", "content": str(output)})
                print(f"🤖:-> {output}")
                
                
        if parsed_response.get("step")=="output":
            print(f"Final output 🤖:-> {parsed_response.get('content')}")
            break
        
        
        
        
        
        

