import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


# @clock
# def soma(x, y):
#     # return [(num + 1) for num in range(10000)]
#     return x + y


class Matematica:
    @clock
    def soma(self, x, y):
        return x + y

# lista = soma()
# print(lista)

# soma = clock(soma)
# print(soma(10, 25))

m = Matematica()
resposta = m.soma(22, 78)
print(resposta)
