# from dotenv import load_dotenv
# from openai import OpenAI
# load_dotenv()
# client = OpenAI()

# text="Dog chases cat"
# response = client.embeddings.create(
#     input=text,
#     model="text-embedding-3-small"
# )
# print(response.data[0].embedding)

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  # Load .env file

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "text-embedding-3-small"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

text="Dog chases cat"

response = client.embeddings.create(
    input=text,
    model=model_name,
)

# for item in response.data:
#     length = len(item.embedding)
#     print(
#         f"data[{item.index}]: length={length}, "
#         f"[{item.embedding[0]}, {item.embedding[1]}, "
#         f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
#     )
# print(response.usage)
print(response) 