from app.parser.python_parser import PythonParser
from app.repository.language import Language

class ParserFactory:
    @staticmethod
    def get(language: Language):
        if language == Language.PYTHON:
            return PythonParser()
        return None