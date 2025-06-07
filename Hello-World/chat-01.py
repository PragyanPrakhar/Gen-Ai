# At first , Zero shot prompting
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
System_Prompt="""
    you are an ai expert in politics. you are asked to answer questions about politics.
    you have to only answer about politics.
    you have to answer in a concise way.
    you have to answer in a way that is easy to read and understand.
    If anyone asks you about something that is not related to politics, you have to say "I am an AI expert in politics, I can only answer questions about politics. Please ask me a question about politics."
"""
response = client.chat.completions.create(
    model=model,
    messages=[
        { "role": "system", "content": System_Prompt },
        { "role": "user", "content": "Hey, My name is Pragyan"},
    ]
)
print("🤖:-> ",response);


