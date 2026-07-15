from app.repository.indexer import RepositoryIndexer
from app.embeddings.service import EmbeddingService
from app.retrieval.vector_store import VectorStore

indexer = RepositoryIndexer()
symbols = indexer.index("./sample_repo")
embedding_service = EmbeddingService()
embeddings = embedding_service.embed(symbols)
store = VectorStore(dimension=len(embeddings[0].vector))
store.add(embeddings)
print("Indexed successfully.")

query = embedding_service.client.embed("authentication")
results = store.search(query)
for result in results:
    print(result.symbol.name)