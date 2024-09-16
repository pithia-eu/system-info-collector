import os

from source.log.logger import logger


def get_env_variable(name):
    value = os.getenv(name)
    if not value:
        logger.error(f"Missing environment variable '{name}'")
        logger.info(f"Program exits with error")
        raise ValueError(f"Missing environment variable '{name}'")
    return value
