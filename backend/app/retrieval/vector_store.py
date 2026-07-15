import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.embeddings = []

    def add(self, embeddings):

        vectors = np.array(
            [e.vector for e in embeddings],
            dtype="float32"
        )

        self.index.add(vectors)

        self.embeddings.extend(embeddings)

    def search(self, vector, k=5):

        vector = np.array(
            [vector],
            dtype="float32"
        )

        distances, indices = self.index.search(vector, k)

        return [
            self.embeddings[i]
            for i in indices[0]
        ]