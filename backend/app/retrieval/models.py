from dataclasses import dataclass
from enum import Enum
from app.repository.language import Language

class ChunkType(str, Enum):
    FUNCTION = "function"
    CLASS = "class"

from dataclasses import dataclass, field
    
@dataclass(slots=True)
class CodeChunk:
    id: str
    file_path: str
    language: Language
    symbol_name: str
    chunk_type: ChunkType
    content: str
    embedding: list[float] = field(default_factory=list)