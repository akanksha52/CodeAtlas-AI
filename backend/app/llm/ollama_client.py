from ollama import chat, embed
from app.core.config import settings
from app.core.logging import logger
from app.core.exception import LLMServiceError

class OllamaClient:
    def __init__(self):
        self.model = settings.ollama_model

    def generate(self, prompt: str) -> str:
        try:
            logger.info(f"Calling Ollama model: {self.model}")
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            logger.info("Received response from Ollama")
            return response["message"]["content"]
        except Exception as e:
            logger.exception("Failed to communicate with Ollama")
            raise LLMServiceError(
                "Unable to communicate with the AI model."
            ) from e
            
    def embed(self, text: str) -> list[float]:
        response = embed(
            model=settings.embedding_model,
            input=text,
        )
        return response["embeddings"][0]