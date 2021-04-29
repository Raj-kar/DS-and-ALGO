# A decorator for monitor total times take a function to get execute
import time


def monitorTime(func):
    """monitor total times take a function to get execute"""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        total = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(round(end_time - start_time, 2), "sec")
        return total
    return wrapper
