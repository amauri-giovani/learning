import time


def stopwatch(func):
    """ Calculates the execution time of the function """
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] ==> Function name: %s' % (elapsed, name))
        return result
    return clocked
