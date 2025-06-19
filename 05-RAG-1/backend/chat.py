# from dotenv import load_dotenv
# from langchain_qdrant import QdrantVectorStore
# from langchain_openai import OpenAIEmbeddings
# from openai import OpenAI

# load_dotenv()

# client = OpenAI()

# # Vector Embeddings
# embedding_model = OpenAIEmbeddings(
#     model="text-embedding-3-large"
# )

# vector_db = QdrantVectorStore.from_existing_collection(
#     url="http://localhost:6333",
#     collection_name="learning_vectors",
#     embedding=embedding_model
# )

# # Take User Query
# query = input("> Enter your Query -> ")

# # Vector Similarity Search [query] in DB
# search_results = vector_db.similarity_search(
#     query=query
# )
# print("Search result is ",search_results)
# # context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])
# context = "\n\n\n".join([
#     f"Page Content: {result.page_content}\nPage Number: {result.metadata.get('page', 'N/A')}\nFile Location: {result.metadata.get('source', 'N/A')}"
#     for result in search_results
# ])

# SYSTEM_PROMPT = f"""
#     You are a helpfull AI Assistant who asnweres user query based on the available context
#     retrieved from a PDF file along with page_contents and page number.

#     You should only ans the user based on the following context and navigate the user
#     to open the right page number to know more.

#     Context:
#     {context}
# """

# chat_completion = client.chat.completions.create(
#     model="gpt-4.1",
#     messages=[
#         { "role": "system", "content": SYSTEM_PROMPT },
#         { "role": "user", "content": query },
#     ]
# )

# print(f"🤖: {chat_completion.choices[0].message.content}")








# from dotenv import load_dotenv
# import os
# from langchain_qdrant import QdrantVectorStore
# from langchain_openai import OpenAIEmbeddings
# from openai import OpenAI

# load_dotenv()

# def generate_answer(query):
#     embedding = OpenAIEmbeddings(
#         model="text-embedding-3-large",
#         openai_api_key=os.getenv("OPENAI_API_KEY")
#     )

#     vector_db = QdrantVectorStore.from_existing_collection(
#         url="http://localhost:6333",
#         collection_name="learning_vectors",
#         embedding=embedding
#     )

#     search_results = vector_db.similarity_search(query)

#     context = "\n\n\n".join([
#         f"📄 Page Content:\n{doc.page_content.strip()}\n"
#         f"📄 Page Number: {doc.metadata.get('page', 'N/A')}\n"
#         f"📁 File: {doc.metadata.get('source', 'N/A')}"
#         for doc in search_results
#     ])

#     SYSTEM_PROMPT = f"""
#     You are a helpful AI Assistant answering user queries based only on the context provided from a PDF.
#     Use the page number and content to guide the user precisely.

#     Context:
#     {context}
#     """

#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#     chat_completion = client.chat.completions.create(
#         model="gpt-4.0",
#         messages=[
#             { "role": "system", "content": SYSTEM_PROMPT },
#             { "role": "user", "content": query },
#         ]
#     )

#     return chat_completion.choices[0].message.content




from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY, QDRANT_URL, COLLECTION_NAME
from vector import get_vector_store

client = OpenAI(api_key=OPENAI_API_KEY)

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=OPENAI_API_KEY)

embedding=embedding_model


def generate_answer(query: str, history: list):
    # search_results = vector_db.similarity_search(query=query)
    vector_db = get_vector_store()
    search_results = vector_db.similarity_search(query=query)

    context = "\n\n".join([
        f"Page Content: {doc.page_content}\nPage Number: {doc.metadata.get('page', 'N/A')}"
        for doc in search_results
    ])

    system_prompt = f"""
    You are a helpful AI Assistant. Answer based on the context provided below and guide the user to the correct page.
    Context:
    {context}
    """

    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": query}]

    chat_response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )

    return {
        "answer": chat_response.choices[0].message.content,
        "source_pages": [doc.metadata.get("page") for doc in search_results]
    }
