from app.core.config import settings
from app.llm.ollama_client import OllamaClient
from app.llm.gemini_client import GeminiClient


class LLMFactory:

    @staticmethod
    def get_client():

        if settings.llm_provider.lower() == "gemini":
            return GeminiClient()

        return OllamaClient()