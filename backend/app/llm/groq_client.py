from openai import OpenAI

from app.core.config import settings
from app.core.exception import LLMServiceError
from app.core.logging import logger


class GroqClient:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.groq_api_key,
            base_url="https://api.groq.com/openai/v1",
        )

        self.model = settings.groq_model

    def generate(self, prompt: str) -> str:
        try:
            logger.info(f"Calling Groq model: {self.model}")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0.2,
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.exception("Failed to communicate with Groq")
            raise LLMServiceError(
                "Unable to communicate with Groq."
            ) from e