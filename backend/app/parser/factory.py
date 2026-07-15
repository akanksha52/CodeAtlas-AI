from app.parser.python_parser import PythonParser
from app.repository.language import Language

class ParserFactory:
    def __init__(self):
        self.parsers = {
            Language.PYTHON: PythonParser(),
    }
    
    def get_parser(self, language: Language):
        return self.parsers.get(language)