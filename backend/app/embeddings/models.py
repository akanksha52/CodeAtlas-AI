from dataclasses import dataclass
from app.repository.symbols import Symbol

@dataclass(slots=True)
class Embedding:
    symbol: Symbol
    vector: list[float]