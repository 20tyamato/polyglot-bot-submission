# src/tools/system_info.py
import multiprocessing

import torch

from src.common import logger


def print_cpu_info():
    cpu_count = multiprocessing.cpu_count()
    logger.info(f"Number of CPU cores: {cpu_count}")


def print_gpu_info():
    if not torch.cuda.is_available():
        logger.info("CUDA is not available.")
        return

    gpu_count = torch.cuda.device_count()
    logger.info(f"Number of GPUs: {gpu_count}")

    for i in range(gpu_count):
        device_name = torch.cuda.get_device_name(i)
        total_memory_mb = torch.cuda.get_device_properties(i).total_memory // (1024**2)
        logger.info(f"GPU-{i}: {device_name}")
        logger.info(f" Memory: {total_memory_mb} MB")


if __name__ == "__main__":
    print_cpu_info()
    print_gpu_info()
