from app.llm.ollama_client import OllamaClient
from app.retrieval.vector_store import VectorStore
from app.core.config import settings

class Retriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
        self.client = OllamaClient()

    def retrieve(
        self,
        question: str,
        k: int = 5,
    ):
        embedding = self.client.embed(question)
        return self.vector_store.search(
            embedding,
            k=k,
            threshold=settings.retrieval_threshold,
        )