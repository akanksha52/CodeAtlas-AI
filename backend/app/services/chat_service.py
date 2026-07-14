from app.llm.ollama_client import OllamaClient
from app.core.logging import logger

class ChatService:
    def __init__(self):
        self.client = OllamaClient()

    def chat(self, message: str) -> str:
        logger.info("Received chat request")
        response = self.client.generate(message)
        logger.info("Successfully generated response")
        return response