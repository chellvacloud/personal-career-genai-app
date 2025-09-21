import os
from src.assistant.config_loader import ConfigLoader
from src.assistant.logger import get_logger


def test_config():
    print("Hello! Starting config test...")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "config.properties")

    # Create config file if it doesn't exist
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w") as f:
            f.write("# Default config properties\n")
            f.write("log_level=INFO\n")
            f.write("log_file=app.log\n")
        print(f"Default config file created at: {config_path}")

    try:
        cfg = ConfigLoader(config_path)
        print("ConfigLoader initialized successfully!")

        if hasattr(cfg, "config"):
            print("Loaded properties:")
            for section in cfg.config.sections():
                for k, v in cfg.config.items(section):
                    print(f"  {k} = {v}")
            # also print defaults
            for k, v in cfg.config.defaults().items():
                print(f"  {k} = {v}")
        else:
            print("ConfigLoader does not expose properties directly. Object:", cfg)
    except FileNotFoundError as e:
        print("Error:", e)


def test_logger():
    print("\nHello! Starting logger test...")
    logger = get_logger(__name__)

    logger.debug("DEBUG log (may not show if level=INFO).")
    logger.info("INFO log from test_logger.")
    logger.warning("WARNING log from test_logger.")
    logger.error("ERROR log from test_logger.")
    logger.critical("CRITICAL log from test_logger.")


def main():
    test_config()
    test_logger()


if __name__ == "__main__":
    main()
