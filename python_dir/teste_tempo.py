import threading
from time import sleep, perf_counter

#
# def verifica(t0):
#     # t0 = perf_counter()
#     elapsed = perf_counter() - t0
#     sleep(1)
#     return elapsed >= 5
#


#
#
# def chama_funcao():
#     for i in range(3):
#         t0 = perf_counter()
#         thread_start = threading.Thread(target=verifica(t0))
#         thread_start.start()
#         # if thread_start:
#         #     continue
#         print(funcao(i))
#
# chama_funcao()

def clock(func):
    def clocked(*args):
        t0 = perf_counter()
        result = func(*args)
        elapsed = perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def funcao(x):
    a = 1
    sleep(1)
    b = 2
    sleep(1)
    return a + b + x


funcao(10)
