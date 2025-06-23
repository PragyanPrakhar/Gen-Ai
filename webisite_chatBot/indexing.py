from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from fetching_links import get_manual_links
from dotenv import load_dotenv

load_dotenv()

# Step 1: Get all internal URLs
# base_url = "https://docs.chaicode.com/"
all_links = get_manual_links()

# Optional: limit the number of pages during development
all_links = all_links[:15]

# Step 2: Load content from all links
loader = WebBaseLoader(all_links)
docs = loader.load()

# Step 3: Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=300
)
split_docs = splitter.split_documents(docs)

# Step 4: Embedding & Storing
embedding = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",  # Or vector-db:6333 if in Docker
    collection_name="chaicode_docs",
    embedding=embedding
)

print("✅ Chaicode docs indexed successfully.")
