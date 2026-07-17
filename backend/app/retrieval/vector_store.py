import faiss
import numpy as np

from app.retrieval.models import CodeChunk


class VectorStore:

    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks: list[CodeChunk] = []

    def add(self, chunks: list[CodeChunk]) -> None:

        vectors = np.array(
            [chunk.embedding for chunk in chunks],
            dtype=np.float32,
        )

        self.index.add(vectors)
        self.chunks.extend(chunks)

    def search(
        self,
        embedding: list[float],
        k: int = 5,
    ) -> list[CodeChunk]:

        query = np.array(
            [embedding],
            dtype=np.float32,
        )

        _, indices = self.index.search(query, k)

        return [
            self.chunks[i]
            for i in indices[0]
            if i != -1
        ]