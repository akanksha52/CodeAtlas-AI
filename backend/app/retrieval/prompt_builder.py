from app.retrieval.models import CodeChunk

class PromptBuilder:
    def build(
        self,
        question: str,
        chunks: list[CodeChunk],
    ) -> str:
        context = ""
        for chunk in chunks:
            context += (
                f"\nFile: {chunk.file_path}\n"
                f"Symbol: {chunk.symbol_name}\n\n"
                f"{chunk.content}\n"
            )
            return f"""
            You are an AI software engineer.

            Answer ONLY using the repository context below.

            If the answer cannot be found in the context, say:
            "I couldn't find that in the repository."

            Repository Context:
            {context}

            Question:
            {question}
            """