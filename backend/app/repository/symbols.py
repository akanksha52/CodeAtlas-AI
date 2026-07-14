from dataclasses import dataclass

@dataclass(slots=True)
class FunctionSymbol:
    name: str
    start_line: int
    end_line: int