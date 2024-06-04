from time import time


def measure_time(func):
    def wrapper(*args):
        start = time()
        func(args[0]) if len(args) > 0 else func()
        return time() - start
    return wrapper
