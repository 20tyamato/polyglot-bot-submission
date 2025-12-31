# src/tools/debug_decorators.py
import functools
import time
import tracemalloc

from src.common import logger


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


if __name__ == "__main__":
    # python src/tools/model_names.py
    # リスト内包表記を使用：すべての要素をメモリに格納
    # range(n) の各値をリストに格納するため、全 100,000 個の整数がメモリに保存されます。これにより空間計算量は O(n) です。
    @measure_time
    @memory_trace
    def sum_with_list(n):
        lst = [i for i in range(n)]
        return sum(lst)

    # ジェネレーター式を使用：要素を逐次生成
    # ジェネレーター式 i for i in range(n) は値を都度生成するため、大量の中間データをメモリに保持せず、空間計算量は O(1) に近いです。
    @measure_time
    @memory_trace
    def sum_with_generator(n):
        return sum(i for i in range(n))

    n = 100000
    logger.info("List version:", sum_with_list(n))
    logger.info("Generator version:", sum_with_generator(n))

    # 再帰的アプローチ（指数関数的）
    # 再帰的に計算する方法はシンプルですが、同じ値の計算を何度も繰り返すため、n が大きくなると計算時間が急激に増加します。
    def fibonacci_recursive_helper(n):
        if n < 2:
            return n
        return fibonacci_recursive_helper(n - 1) + fibonacci_recursive_helper(n - 2)

    @measure_time
    def fibonacci_recursive(n):
        return fibonacci_recursive_helper(n)

    # 動的計画法（反復的／線形）
    # ループを利用して順次値を更新する方法は、各計算を一度ずつ行うので、入力サイズに対して線形の時間計算量となります。
    @measure_time
    def fibonacci_iterative(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    n = 20  # 再帰版では n=20 程度が現実的です
    logger.info("Naive Recursive Fibonacci:", fibonacci_recursive(n))
    logger.info("Iterative Fibonacci:", fibonacci_iterative(n))
