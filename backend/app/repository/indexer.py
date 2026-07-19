from pathlib import Path
from dataclasses import dataclass, field

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

        print("=" * 70)
        print("FILES FOUND:", len(files))

        for repository_file in files:
            print(f"\nFILE: {repository_file.path}")
            print("LANGUAGE:", repository_file.language)

            parser = self.factory.get_parser(repository_file.language)

            if parser is None:
                print("NO PARSER")
                continue

            code = Path(repository_path, repository_file.path).read_bytes()

            repository_file.symbols = parser.parse(code)

            print("SYMBOL COUNT:", len(repository_file.symbols))

            for symbol in repository_file.symbols:
                print(type(symbol).__name__, getattr(symbol, "name", ""))

        print("=" * 70)

        return RepositoryIndex(files=files)