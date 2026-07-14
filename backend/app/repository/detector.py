from pathlib import Path
from app.repository.language import Language
from app.repository.constants import EXTENSION_TO_LANGUAGE

class LanguageDetector:
    def detect(self, path: Path) -> Language:
        return EXTENSION_TO_LANGUAGE.get(
            path.suffix.lower(),
            Language.UNKNOWN,
        )