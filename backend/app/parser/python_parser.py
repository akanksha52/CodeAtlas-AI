from tree_sitter import Language as TSLanguage, Parser
import tree_sitter_python as tspython
from app.repository.symbols import FunctionSymbol, ClassSymbol, ImportSymbol
from app.parser.base import CodeParser
from app.repository.language import Language
from app.repository.symbols import Symbol
from tree_sitter import Node

PY_LANGUAGE = TSLanguage(tspython.language())

class PythonParser(CodeParser):
    def __init__(self):
        self.parser = Parser(PY_LANGUAGE)
        
    def _node_text(self, node, code: bytes,) -> str:
        return code[node.start_byte:node.end_byte].decode("utf-8")
    
    def parse(self, code: bytes) -> list[Symbol]:
        tree = self.parser.parse(code)
        root = tree.root_node
        symbols: list[Symbol] = []
        self._extract_symbols(root, code, symbols,)
        return symbols
    
    def _extract_symbols(self, node: Node, code: bytes, symbols: list[Symbol],):
        self._extract_function(node, code, symbols,)
        self._extract_class(node, code, symbols,)
        self._extract_import(node, code, symbols,)
        for child in node.children:
            self._extract_symbols(child, code, symbols,)

    def _extract_function(self, node, code, symbols,):
        if node.type != "function_definition":
            return
        for child in node.children:
            if child.type == "identifier":
                name = self._node_text(child, code)
            elif child.type == "parameters":
                parameters = self._node_text(child, code)
        source_code = code[node.start_byte:node.end_byte].decode("utf-8")
        signature = f"{name}{parameters}"
        symbols.append(FunctionSymbol(name=name, signature=signature, source_code=source_code, start_line=node.start_point[0] + 1,
        end_line=node.end_point[0] + 1,))
        
    def _extract_class(self, node, code, symbols,):
        if node.type != "class_definition":
            return
        for child in node.children:
            if child.type == "identifier":
                name = self._node_text(child, code)
        source_code = code[node.start_byte:node.end_byte].decode("utf-8")
        symbols.append(ClassSymbol(name=name, start_line=node.start_point[0] + 1, end_line=node.end_point[0] + 1, source_code = source_code))
                
    def _extract_import(self, node: Node, code: bytes, symbols: list[Symbol]):
        if node.type == "import_statement":
            source_code = self._node_text(node, code)
            for child in node.children:
                if child.type == "dotted_name":
                    symbols.append(ImportSymbol(name=self._node_text(child, code), source_code=source_code,))
        elif node.type == "import_from_statement":
            source_code = self._node_text(node, code)
            module = None
            for child in node.children:
                if child.type == "dotted_name":
                    module = self._node_text(child, code)
                    break
            if module is not None:
                symbols.append(ImportSymbol(name=module, source_code=source_code,))