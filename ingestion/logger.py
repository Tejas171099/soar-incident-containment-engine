import logging
import sys


def setup_logger() -> logging.Logger:
    """
    Configure application-wide logging for the SOAR enrichment service.
    """

    logger = logging.getLogger("soar")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
