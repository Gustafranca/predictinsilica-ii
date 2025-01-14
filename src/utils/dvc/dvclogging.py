"""File to configure the logs for the DVC pipeline."""
import logging


def configure_logging():
    """Configure the logs for the DVC pipeline."""
    # Configure the logs file
    # pylint: disable=logging-fstring-interpolation
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Create a file handler and set the level to debug
    file_handler = logging.FileHandler("logs/dvc_logs.log")
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)

    # Get the root logger and add the handlers
    logger = logging.getLogger()
    logger.addHandler(file_handler)
