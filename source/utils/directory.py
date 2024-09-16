import os

from source.log.logger import logger


def create_local_directory(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory, mode=0o777)
            logger.debug(f"Directory created: {directory}")
        except PermissionError:
            logger.exception(f"Permission denied when trying to create directory: {directory}",
                             exc_info=True)
            raise
    else:
        logger.debug(f"Directory exists: {directory}")
