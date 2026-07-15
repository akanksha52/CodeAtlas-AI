from app.repository.indexer import RepositoryIndexer

indexer = RepositoryIndexer()

symbols = indexer.index("sample_repo")   # change path

print(f"Found {len(symbols)} symbols")

for symbol in symbols:
    print(symbol)