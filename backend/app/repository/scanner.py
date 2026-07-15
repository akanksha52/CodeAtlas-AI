from pathlib import Path
from app.repository.constants import IGNORED_DIRECTORIES, SUPPORTED_EXTENSIONS
from app.repository.models import RepositoryFile
from app.repository.detector import LanguageDetector

detector=LanguageDetector()

class RepositoryScanner:
    def scan(self, repository_path: str):
        repository = Path(repository_path)
        files = []
        for path in repository.rglob("*"):
            if any(part in IGNORED_DIRECTORIES for part in path.parts):
                continue
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
                files.append(RepositoryFile(path=path, language=detector.detect(path)))
            files.sort(key=lambda file: file.path)
        return files