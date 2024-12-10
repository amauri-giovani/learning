import time
from functools import wraps


def timethis(func):
    """
    Decorador que informa o tempo de execução
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # print(func.__name__, end - start)
        print(func.__name__, round(end - start, 2))
        return result
    return wrapper


@timethis
def countdown(n):
    """
    Faz a contagem decrescente
    """
    while n > 0:
        n -= 1

countdown(300000)