from pathlib import Path

from app.parser.factory import ParserFactory
from app.repository.scanner import RepositoryScanner


class RepositoryService:
    def __init__(self):
        self.scanner = RepositoryScanner()

    def analyze(self, repository_path: str):
        files = self.scanner.scan(repository_path)
        for repository_file in files:
            code = Path(repository_path, repository_file.path).read_bytes()
            parser = ParserFactory.get(repository_file.language)
            if parser is None:
                continue
            repository_file.symbols = parser.parse(code)

        return files