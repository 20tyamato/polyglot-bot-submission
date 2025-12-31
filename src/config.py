# src/config.py
import logging
import logging.config
import os


def init_logging_config():
    config_path = os.getenv("LOG_CONFIG_FILE_PATH")
    if not config_path or not os.path.exists(config_path):
        logging.basicConfig(level=logging.INFO)
        logging.getLogger(__name__).warning(
            "The logging configuration file was not found, using basic configuration."
        )
        return

    try:
        log_file_path = os.getenv("LOG_FILE_PATH", "logs/default.log")
        log_dir = os.path.dirname(log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        if not os.path.exists(log_file_path):
            with open(log_file_path, "w"):
                pass
        defaults = {
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "LOG_FILE_PATH": log_file_path,
        }
        logging.config.fileConfig(
            config_path, disable_existing_loggers=False, defaults=defaults
        )
        third_party_loggers = {
            "httpx": logging.WARNING,
            "httpcore": logging.WARNING,
            "urllib3": logging.WARNING,
            "asyncio": logging.WARNING,
            "google_genai": logging.WARNING,
            "discord": logging.WARNING,
            "discord.http": logging.ERROR,
            "discord.gateway": logging.ERROR,
            "discord.client": logging.ERROR,
            "googleapiclient.discovery_cache": logging.ERROR,
            "googleapiclient": logging.WARNING,
        }
        for logger_name, level in third_party_loggers.items():
            logging.getLogger(logger_name).setLevel(level)
    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger(__name__).exception(
            "Failed to load the logging configuration file, using basic configuration. Error: %s",
            e,
        )
