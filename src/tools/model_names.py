# src/tools/model_names.py
from openai import OpenAI

from src.common import logger
from src.utils import get_env_var


def get_openai_model_names():
    client = OpenAI(api_key=get_env_var("OPENAI_API_KEY"))
    models = client.models.list()
    models.data = sorted(models.data, key=lambda x: x.created)
    model_names = [model.id for model in models.data]
    return model_names


def print_openai_model_names():
    model_names = get_openai_model_names()
    logger.info(model_names)


if __name__ == "__main__":
    # python src/tools/model_names.py
    print_openai_model_names()
