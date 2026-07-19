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
        threshold: float = 1.1,
    ) -> list[CodeChunk]:

        query = np.array(
            [embedding],
            dtype=np.float32,
        )

        distances, indices = self.index.search(query, k)

        results = []

        for dist, idx in zip(distances[0], indices[0]):

            
            if idx == -1:
                continue

            if dist > threshold:
                continue

            results.append(self.chunks[idx])

        return results