from ollama import chat

class OllamaClient:
    def __init__(self, model: str = "qwen2.5-coder:7b"):
        self.model = model

    def generate(self, prompt: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]