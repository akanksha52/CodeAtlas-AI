from google import genai

from app.core.config import settings
from app.core.exception import LLMServiceError
from app.core.logging import logger


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.gemini_model

    def generate(self, prompt: str) -> str:
        try:
            logger.info(f"Calling Gemini model: {self.model}")

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            logger.info("Received response from Gemini")

            return response.text

        except Exception as e:
            logger.exception("Failed to communicate with Gemini")

            raise LLMServiceError(
                "Unable to communicate with Gemini."
            ) from e