from app.repository.indexer import RepositoryIndexer
from app.repository.indexer import RepositoryIndex
from app.retrieval.chunk_builder import ChunkBuilder
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_store import VectorStore
from app.retrieval.models import CodeChunk


class IndexManager:

    def __init__(self):
        self.repository_path: str | None = None
        self.repository_index: RepositoryIndex | None = None
        self.chunks: list[CodeChunk] = []
        self.vector_store: VectorStore | None = None

    def build(self, repository_path: str):
        repository_index = RepositoryIndexer().index(repository_path)
        chunks = ChunkBuilder().build(repository_index)
        chunks = EmbeddingService().embed_chunks(chunks)
        if not chunks:
            raise RuntimeError("No chunks generated.")
        dimension = len(chunks[0].embedding)
        vector_store = VectorStore(dimension)
        vector_store.add(chunks)
        self.repository_path = repository_path
        self.repository_index = repository_index
        self.chunks = chunks
        self.vector_store = vector_store

    def ready(self):
        return self.vector_store is not None
    
    @property
    def files(self):
        return self.repository_index.files

    @property
    def stats(self):
        return {
            "files": len(self.repository_index.files),
            "chunks": len(self.chunks)
        }