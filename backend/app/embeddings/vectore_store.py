import math

from app.retrieval.models import CodeChunk


class VectorStore:
    def __init__(self):
        self.chunks: list[CodeChunk] = []

    def add(self, chunks: list[CodeChunk]) -> None:
        self.chunks.extend(chunks)

    def search(
        self,
        embedding: list[float],
        k: int = 5,
    ) -> list[CodeChunk]:
        scored: list[tuple[float, CodeChunk]] = []
        for chunk in self.chunks:
            similarity = self._cosine_similarity(
                embedding,
                chunk.embedding,
            )
            scored.append(
                (
                    similarity,
                    chunk,
                )
            )
        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )
        return [
            chunk
            for _, chunk in scored[:k]
        ]

    def _cosine_similarity(
        self,
        a: list[float],
        b: list[float],
    ) -> float:
        dot_product = sum(
            x * y
            for x, y in zip(a, b)
        )
        norm_a = math.sqrt(
            sum(x * x for x in a)
        )
        norm_b = math.sqrt(
            sum(y * y for y in b)
        )
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)