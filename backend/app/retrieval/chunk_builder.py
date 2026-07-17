from app.repository.indexer import RepositoryIndex
from app.retrieval.models import CodeChunk
from app.repository.symbols import FunctionSymbol, ClassSymbol

class ChunkBuilder:
    def build(self, index: RepositoryIndex) -> list[CodeChunk]:
        chunks: list[CodeChunk] = []

        for repository_file in index.files:
            for symbol in repository_file.symbols:
                if not isinstance(symbol, (FunctionSymbol, ClassSymbol)):
                    continue

                chunks.append(
                    CodeChunk(
                        id=f"{repository_file.path}:{symbol.name}",
                        file_path=repository_file.path,
                        language=repository_file.language,
                        symbol_name=symbol.name,
                        chunk_type=symbol.__class__.__name__,
                        content=symbol.source_code,
                    )
                )

        return chunks