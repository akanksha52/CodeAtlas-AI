from dataclasses import dataclass
from pathlib import Path
from app.repository.language import Language

@dataclass(slots=True)
class RepositoryFile:
    path: Path
    language: Language