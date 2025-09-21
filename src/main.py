import os
import sys

# -----------------------------
# Add src/ folder to sys.path for right-click run
# -----------------------------
SRC_DIR = os.path.dirname(os.path.abspath(__file__))  # points to src/
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Imports from assistant/ now work
from assistant.config_loader import ConfigLoader
from assistant.logger import get_logger
from services.google_genai_service import GoogleAIService


def main():
    print("=== Starting App ===")

    # 1. Load Config
    PROJECT_ROOT = os.path.dirname(SRC_DIR)
    config_path = os.path.join(PROJECT_ROOT, "config", "config.properties")
    cfg = ConfigLoader(config_path)
    print("Config loaded successfully!")

    # 2. Setup Logger
    logger = get_logger(__name__)
    logger.info("Logger initialized successfully.")

    # 3. Google GenAI Service
    try:
        google_api_key = cfg.get("GOOGLE_API_KEY")  # read from config.properties
        google_ai = GoogleAIService(api_key=google_api_key)

        prompt = "Write a 2-line motivational quote about learning AI."
        response = google_ai.generate_text(prompt)

        logger.info("Google GenAI responded successfully.")
        print("\n--- Google GenAI Output ---")
        print(response)

    except Exception as e:
        logger.error(f"Google GenAI failed: {e}")
        print("Google GenAI Test Failed:", e)


if __name__ == "__main__":
    main()
