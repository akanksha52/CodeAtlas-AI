from app.repository.indexer import RepositoryIndex
from app.repository.indexer import RepositoryIndexer


class RepositoryService:
    def __init__(self):
        self.indexer = RepositoryIndexer()

    def analyze(self, repository_path: str) -> RepositoryIndex:
        return self.indexer.index(repository_path)