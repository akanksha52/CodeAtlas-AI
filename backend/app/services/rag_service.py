from app.llm.factory import LLMFactory
from app.retrieval.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever
from app.services.index_manager import IndexManager


class RAGService:

    def __init__(self, manager: IndexManager):
        self.manager = manager
        self.prompt_builder = PromptBuilder()
        self.client = LLMFactory.get_client()

    def ask(self, question: str):

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

        answer = self.client.generate(prompt)

        sources = []

        seen = set()

        for chunk in chunks:

            key = (
                chunk.file_path,
                chunk.symbol_name,
            )

            if key in seen:
                continue

            seen.add(key)
            
            sources.append(
                {
                    "file": str(chunk.file_path),
                    "symbol": chunk.symbol_name,
                    "type": (
                        chunk.chunk_type.value
                        if hasattr(chunk.chunk_type, "value")
                        else str(chunk.chunk_type)
                    ),
                }
            )

        return {
            "response": answer,
            "sources": sources,
        }