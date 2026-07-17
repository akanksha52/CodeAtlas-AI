from pathlib import Path
from app.repository.constants import (
    IGNORED_DIRECTORIES,
    SUPPORTED_EXTENSIONS,
)
from app.repository.detector import LanguageDetector
from app.repository.models import RepositoryFile

detector = LanguageDetector()


class RepositoryScanner:
    def scan(self, repository_path: str) -> list[RepositoryFile]:
        repository = Path(repository_path)
        files: list[RepositoryFile] = []
        for path in repository.rglob("*"):
            if any(part in IGNORED_DIRECTORIES for part in path.parts):
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue
            relative_path = path.relative_to(repository)
            files.append(
                RepositoryFile(
                    path=relative_path,
                    language=detector.detect(path),
                )
            )
        files.sort(key=lambda file: str(file.path))
        return files