import os
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_NAME = "collect"
DEFAULT_LOG_PATH = "log/main.log"
DEFAULT_LOG_LEVEL = logging.DEBUG
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEFAULT_MAX_BYTES = 100000
DEFAULT_BACKUP_COUNT = 5


def _setup_logger(log_name=DEFAULT_LOG_NAME,
                  file_path=DEFAULT_LOG_PATH,
                  log_level=DEFAULT_LOG_LEVEL,
                  log_format=DEFAULT_LOG_FORMAT,
                  max_bytes=DEFAULT_MAX_BYTES,
                  backup_count=DEFAULT_BACKUP_COUNT):
    _logger = logging.getLogger(log_name)
    _logger.setLevel(log_level)
    c_handler = _create_console_handler(log_format,
                                        log_level)
    _logger.addHandler(c_handler)
    f_handler = _create_file_handler(_logger,
                                     backup_count,
                                     file_path,
                                     log_format,
                                     log_level,
                                     max_bytes)
    _logger.addHandler(f_handler)
    return _logger


def _create_console_handler(log_format,
                            log_level):
    c_handler = logging.StreamHandler()
    c_handler.setLevel(log_level)
    c_formatter = logging.Formatter(log_format)
    c_handler.setFormatter(c_formatter)
    return c_handler


def _create_file_handler(_logger,
                         backup_count,
                         file_path,
                         log_format,
                         log_level,
                         max_bytes):
    directory = os.path.dirname(os.path.abspath(file_path))
    if not os.path.exists(directory):
        _logger.error(f"Directory {directory} does not exist.")
        try:
            os.makedirs(directory)
            _logger.info('Directory created')
        except OSError as e:
            _logger.exception("Failed to create log directory",
                              exc_info=True)
            _logger.info(f"Program exits with error")
            raise
    if not os.access(directory, os.W_OK):
        _logger.error(f"Script does not have write access to the directory {directory}.")
        _logger.info(f"Program exits with error")
        raise PermissionError(f"Script does not have write access to the directory {directory}.")
    try:
        f_handler = RotatingFileHandler(file_path,
                                        maxBytes=max_bytes,
                                        backupCount=backup_count)
    except PermissionError:
        _logger.exception("There is no write permission to create a log file at this path.",
                          exc_info=True)
        _logger.info(f"Program exits with error")
        raise
    except FileNotFoundError:
        _logger.exception("The provided file path does not exist.",
                          exc_info=True)
        _logger.info(f"Program exits with error")
        raise
    f_handler.setLevel(log_level)
    f_formatter = logging.Formatter(log_format)
    f_handler.setFormatter(f_formatter)
    return f_handler


logger = _setup_logger()
