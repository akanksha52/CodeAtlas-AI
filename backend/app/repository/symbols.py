from dataclasses import dataclass

@dataclass(slots=True)
class Symbol:
    name: str
    source_code: str

@dataclass(slots=True)
class FunctionSymbol(Symbol):
    start_line: int
    end_line: int
    signature: str
    
@dataclass(slots=True)
class ClassSymbol(Symbol):
    start_line: int
    end_line: int
    
@dataclass(slots=True)
class ImportSymbol(Symbol):
    pass