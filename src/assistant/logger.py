import logging
import os

# Default log directory and file
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")

def setup_logger(name: str) -> logging.Logger:
    """Setup a logger with console + file handlers."""
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

    # File handler
    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

    # Attach handlers
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def get_logger(name: str) -> logging.Logger:
    """Public API to fetch a configured logger."""
    return setup_logger(name)
