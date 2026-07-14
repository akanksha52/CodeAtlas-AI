from tree_sitter import Language, Parser
import tree_sitter_python as tspython
from app.repository.symbols import FunctionSymbol
from tree_sitter import Language, Parser
import tree_sitter_python as tspython
from app.repository.symbols import FunctionSymbol

PY_LANGUAGE = Language(tspython.language())

class PythonParser:
    def __init__(self):
        self.parser = Parser(PY_LANGUAGE)
    
    def parse(self, code: bytes):
        tree = self.parser.parse(code)
        root = tree.root_node
        symbols = []
        for node in root.children:
            if node.type != "function_definition":
                continue
            for child in node.children:
                if child.type == "identifier":
                    name = code[
                        child.start_byte: child.end_byte
                        ].decode("utf-8")
                    symbols.append(
                        FunctionSymbol(
                            name=name,
                            start_line=node.start_point[0] + 1,
                            end_line=node.end_point[0] + 1,
                        )
                    )
        return symbols