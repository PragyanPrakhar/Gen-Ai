from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Vector Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Load from existing Qdrant collection
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="chaicode_docs",
    embedding=embedding_model
)

# Take User Query
query = input("> ")

# Vector Similarity Search
search_results = vector_db.similarity_search(query=query)

# Format retrieved context
context = "\n\n\n".join([
    f"Page Content: {doc.page_content}\nSource URL: {doc.metadata.get('source', 'N/A')}"
    for doc in search_results
])

# Prompt for LLM
SYSTEM_PROMPT = f"""
You are a helpful AI assistant that answers user queries using the provided website context only.
Each chunk is from the Chaicode documentation, and may include page content and source URLs.

Use only the context provided below to answer. If the answer is not present, say you don't know.

Context:
{context}
"""

# Call OpenAI Chat Completion API
chat_completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": query },
    ]
)

# Show the response
print(f"\n🤖: {chat_completion.choices[0].message.content}")
