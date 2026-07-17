from dataclasses import dataclass, field
from pathlib import Path

from app.parser.factory import ParserFactory
from app.repository.models import RepositoryFile
from app.repository.scanner import RepositoryScanner


@dataclass(slots=True)
class RepositoryIndex:
    files: list[RepositoryFile] = field(default_factory=list)

class RepositoryIndexer:
    def __init__(self):
        self.scanner = RepositoryScanner()
        self.factory = ParserFactory()
        
    def index(self, repository_path: str) -> RepositoryIndex:
        files = self.scanner.scan(repository_path)
        for repository_file in files:
            parser = self.factory.get_parser(repository_file.language)
            if parser is None:
                continue
            code = Path(repository_path, repository_file.path).read_bytes()
            repository_file.symbols = parser.parse(code)
        return RepositoryIndex(files=files)