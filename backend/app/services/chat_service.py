from app.llm.ollama_client import OllamaClient

class ChatService:
    def __init__(self):
        self.client = OllamaClient()

    def chat(self, message: str) -> str:
        return self.client.generate(message)