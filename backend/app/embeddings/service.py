from app.embeddings.models import Embedding
from app.llm.embedding_client import OllamaEmbeddingClient


class EmbeddingService:

    def __init__(self):
        self.client = OllamaEmbeddingClient()

    def embed(self, symbols):
        embeddings = []
        for symbol in symbols:
            text = self._to_text(symbol)
            vector = self.client.embed(text)
            embeddings.append(Embedding(symbol=symbol, vector=vector,))
        return embeddings

    def _to_text(self, symbol):
        return symbol.source_code