from tree_sitter import Language, Parser
import tree_sitter_python as tspython

PY_LANGUAGE = Language(tspython.language())

class PythonParser:
    def __init__(self):
        self.parser = Parser(PY_LANGUAGE)
        
