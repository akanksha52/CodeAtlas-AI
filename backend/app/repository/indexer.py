from pathlib import Path
from app.parser.factory import ParserFactory
from app.repository.scanner import RepositoryScanner

class RepositoryIndexer:
    def __init__(self):
        self.scanner = RepositoryScanner()
        self.factory = ParserFactory()

    def index(self, path):
        files = self.scanner.scan(path)
        all_symbols = []
        for file in files:
            parser = self.factory.get_parser(file.language)
            if parser is None:
                continue
            code = Path(file.path).read_bytes()
            symbols = parser.parse(code)
            all_symbols.extend(symbols)
        return all_symbols