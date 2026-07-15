from dataclasses import dataclass, field
from pathlib import Path
from app.repository.language import Language
from app.repository.symbols import Symbol

@dataclass(slots=True)
class RepositoryFile:
    path: Path
    language: Language
    symbols: list[Symbol] = field(default_factory=list)