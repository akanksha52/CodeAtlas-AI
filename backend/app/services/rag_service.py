from app.llm.ollama_client import OllamaClient
from app.retrieval.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever
from app.services.index_manager import IndexManager


class RAGService:
    def __init__(self, manager: IndexManager):
        self.manager = manager
        self.prompt_builder = PromptBuilder()
        self.ollama = OllamaClient()

    def ask(self, question: str) -> str:
        if not self.manager.ready():
            raise RuntimeError(
                "Repository has not been indexed yet."
            )
        retriever = Retriever(
            self.manager.vector_store
        )
        chunks = retriever.retrieve(question)
        prompt = self.prompt_builder.build(
            question=question,
            chunks=chunks,
        )
        return self.ollama.generate(prompt)