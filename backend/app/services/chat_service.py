from app.core.logging import logger
from app.llm.factory import LLMFactory

class ChatService:
    def __init__(self):
        self.client = LLMFactory.get_client()

    def chat(self, message: str) -> str:
        logger.info("Received chat request")
        response = self.client.generate(message)
        logger.info("Successfully generated response")
        return response