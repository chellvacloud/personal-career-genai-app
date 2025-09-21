import os
from openai import OpenAI
from src.assistant.logger import get_logger

logger = get_logger(__name__)

class OpenAIService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided. Set OPENAI_API_KEY in env.")
        self.client = OpenAI(api_key=self.api_key)
        logger.info("OpenAIService initialized.")

    def generate_text(self, prompt: str, model: str = "gpt-4o-mini") -> str:
        """Generate text using OpenAI."""
        try:
            logger.debug(f"Sending prompt to OpenAI: {prompt}")
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAIService error: {e}")
            return f"Error: {e}"
