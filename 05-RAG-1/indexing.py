from dotenv import load_dotenv
from pathlib import Path
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from custom_embeddings import GitHubEmbeddings
from openai import OpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings


from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct

load_dotenv()  # Load .env file

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference" 

embedding_model_name = "text-embedding-3-large"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# # Init custom embedding model
# embedding_model = GitHubEmbeddings(endpoint=endpoint, github_token=token)


pdf_path=Path(__file__).parent / "nodejs.pdf"

# Here we will load the pdf file and convert it into text
loader = PyPDFLoader(file_path=pdf_path)
docs=loader.load()

print(f"Loaded {len(docs)} documents from {pdf_path}")
# for doc in docs:
#     print(f"Document content: {doc.page_content[:100]}...")  # Print first 100 characters of each document
#     print(f"Metadata: {doc.metadata}")  # Print metadata of the document

# Now we will do the chunking of the documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

split_docs = text_splitter.split_documents(documents=docs)

print(f"Split into {len(split_docs)} chunks")

# Now we will create the embeddings for the split documents
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# response = client.embeddings.create(
#     input=["first phrase", "second phrase", "third phrase"],
#     model=model_name,
# )




# here we will use the above model to create the embeddings of the split docs and store them in a vector store.
vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding,
)
client1 = QdrantClient(url="http://localhost:6333")  # adjust URL
collection_info = client1.get_collection(collection_name="learning_vectors")


print("✅ Indexing completed with GitHub-hosted embeddings.")


print("Quadrant Client payload",collection_info.payload_schema)  # info about stored data
print("Quadrant client payloadddddddddd",collection_info.vectors_count)  