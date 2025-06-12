import httpx
from typing import List
from langchain_core.embeddings import Embeddings

class GitHubEmbeddings(Embeddings):
    def __init__(self, github_token: str, endpoint: str, model: str = "text-embedding-3-large"):
        self.token = github_token
        self.endpoint = endpoint.rstrip("/")
        self.model = model

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._embed(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._embed(text)

    def _embed(self, text: str) -> List[float]:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "input": [text]
        }

        response = httpx.post(f"{self.endpoint}/embeddings", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]
