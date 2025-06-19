# db/vector.py
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

def get_vector_store():
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
    return QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        collection_name="learning_vectors",
        embedding=embedding_model
    )
