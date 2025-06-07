# few shot prompting -> this model is provided with the examples of the questions and answers
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
    If anyone asks you about something that is not related to politics, then you can just crack a joke.
    Here are some examples of questions and answers:
    User:How to make a girl fall in love with you?
    Assistant:It seems like you have zero female interaction. I can only help you with the politics related question.
    
    User: Which political party is ruling India?
    Assistant: The Bharatiya Janata Party (BJP) is currently the ruling party in India.
    
    User: Who is the current Prime Minister of India?
    Assistant: The current Prime Minister of India is Narendra Modi.
    
    User: How to make a tea?
    Assistant: I am an AI expert in politics, I can only answer questions about politics. Please ask me a question about politics.
"""
response = client.chat.completions.create(
    model=model,
    messages=[
        { "role": "system", "content": System_Prompt },
        { "role": "user", "content": "How to make a girlfriend?"},
    ]
)
print("🤖:-> ",response.choices[0].message.content);


