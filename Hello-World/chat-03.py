# chain of thought reasoning ->   Providing a CoT (Chain of Thought) prompt involves guiding the model to reason step-by-step instead of jumping straight to the final answer. This technique improves reasoning quality, especially for tasks involving logic, math, or complex decisions.
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
    Q: Write a function to check if a number is a palindrome.

    Let’s think step by step.

    Step 1: Understand what a palindrome is. A number is a palindrome if it reads the same forward and backward (e.g., 121 or 909).

    Step 2: Convert the number to a string.

    Step 3: Compare the string with its reverse.

    Step 4: Return True if they match, else return False.

    Answer (in Python):
    def is_palindrome(n):
    return str(n) == str(n)[::-1]

"""
response = client.chat.completions.create(
    model=model,
    messages=[
        { "role": "system", "content": System_Prompt },
        { "role": "user", "content": "Hi, , can you write to check whether a number is armstrong or not?" },
    ]
)
print("🤖:-> ",response.choices[0].message.content);

