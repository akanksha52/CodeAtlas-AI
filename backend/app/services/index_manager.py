from app.repository.indexer import RepositoryIndexer
from app.retrieval.chunk_builder import ChunkBuilder
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_store import VectorStore

class IndexManager:
    def __init__(self):
        self.vector_store = None
        self.repository_path = None

    def build(self, repository_path: str):
        index = RepositoryIndexer().index(
            repository_path
        )
        chunks = ChunkBuilder().build(index)
        chunks = EmbeddingService().embed_chunks(
            chunks
        )
        if not chunks:
            raise RuntimeError(
                "Repository contains no indexable code."
            )
        dimension = len(chunks[0].embedding)
        self.vector_store = VectorStore(
            dimension
        )
        self.vector_store.add(chunks)
        self.repository_path = repository_path

    def ready(self) -> bool:
        return self.vector_store is not None