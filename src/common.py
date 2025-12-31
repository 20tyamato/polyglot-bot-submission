# src/common.py
import functools
import logging
import os
import time
import tracemalloc

from dotenv import load_dotenv

from src.config import init_logging_config

load_dotenv()
init_logging_config()

logger = logging.getLogger(__name__)


def get_env_var(var_name: str) -> str:
    env_var = os.environ.get(var_name)
    if not env_var:
        err_msg = f"{var_name} is not set in the environment variables."
        logger.error(err_msg)
        raise EnvironmentError(err_msg)
    return env_var


def memory_trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        logger.info(f"[{func.__name__}] Current memory usage: {current / 1024:.2f} KB")
        logger.info(f"[{func.__name__}] Peak memory usage: {peak / 1024:.2f} KB")
        return result

    return wrapper


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"[{func.__name__}] Execution time: {execution_time:.6f} seconds")
        return result

    return wrapper


SUPPORTED_LANGUAGES = {
    "en": {
        "name": "English",
        "emoji": "🇺🇸🇬🇧",
        "description": "to translate to English",
    },
    "jp": {
        "name": "Japanese",
        "emoji": "🇯🇵",
        "description": "to translate to Japanese",
    },
}

GLOSSARY_JSON = """
{
  "buff": "強化",
  "nerf": "弱体化",
  "bug": "不具合",
  "glitch": "バグ",
  "build": "ビルド",
  "hotfix": "緊急修正"
}
"""
