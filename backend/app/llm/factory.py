from app.core.config import settings
from app.llm.groq_client import GroqClient
from app.llm.ollama_client import OllamaClient

class LLMFactory:

    @staticmethod
    def get_client():
        provider = settings.llm_provider.lower()
        if provider == "ollama":
            return OllamaClient()

        if provider == "groq":
            return GroqClient()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )