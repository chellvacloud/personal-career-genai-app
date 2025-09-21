import os
import google.generativeai as genai
from assistant.logger import get_logger  # <-- fixed import (no src prefix)

logger = get_logger(__name__)


class GoogleAIService:
    def __init__(self, api_key: str = None):
        """
        Initialize GoogleAIService with API key.
        Priority:
        1. api_key passed explicitly (from config.properties via main.py)
        2. GOOGLE_API_KEY from environment
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API key not provided in config.properties or environment.")

        genai.configure(api_key=self.api_key)
        logger.info("GoogleAIService initialized successfully.")

    def generate_text(self, prompt: str, model: str = "gemini-1.5-flash") -> str:
        """
        Generate text using Google Gemini model.
        """
        try:
            logger.debug(f"Sending prompt to Google GenAI model={model}: {prompt}")
            model_instance = genai.GenerativeModel(model)
            response = model_instance.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"GoogleAIService error: {e}")
            return f"Error: {e}"
