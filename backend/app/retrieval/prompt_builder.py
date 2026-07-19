from app.retrieval.models import CodeChunk


class PromptBuilder:

    def build(
        self,
        question: str,
        chunks: list[CodeChunk],
    ) -> str:

        if not chunks:
            return f"""
You are an expert software engineer.

The user asked a question that is not answered by the indexed repository.

Answer using your general software engineering knowledge.

If the question is unrelated to programming, politely say so.

Question:
{question}
"""

        context = ""

        for chunk in chunks:
            context += (
                f"\n===== FILE =====\n"
                f"File: {chunk.file_path}\n"
                f"Symbol: {chunk.symbol_name}\n"
                f"Type: {chunk.chunk_type}\n\n"
                f"{chunk.content}\n"
            )

        return f"""
You are an AI Code Intelligence Assistant.

Your job is to help developers understand codebases.

Repository Context:
{context}

User Question:
{question}

Instructions:

- Base your answer primarily on the repository context.
- Explain classes, functions and relationships clearly.
- If the repository contains only part of the answer, say so and then use your software engineering knowledge to complete the explanation.
- If the repository does not contain enough information, clearly mention that before answering using general programming knowledge.
- Never invent repository details that are not present.
- Format your response using Markdown.
- Use bullet points where appropriate.
- Include short code snippets if helpful.
"""