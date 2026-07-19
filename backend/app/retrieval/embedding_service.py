from app.llm.ollama_client import OllamaClient
from app.retrieval.models import CodeChunk

class EmbeddingService:
    def __init__(self):
        self.client = OllamaClient()

    def embed_chunks(
        self,
        chunks: list[CodeChunk],
    ) -> list[CodeChunk]:
        for chunk in chunks:
            chunk.embedding = self.client.embed(
                chunk.content
            )
        return chunks