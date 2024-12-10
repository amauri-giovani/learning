def f(a, b, c='dC', *args, **kwargs):
    print(a, b, c, args, kwargs)

    """
    Retorna
    A B C ('D', 'E') {'z': 'Z', 'w': 'W'}
    """

f('A', 'B', 'C', 'D', 'E', z='Z', w='W')


def filter(**lookups):
    for k, v in lookups.items():
        print(k)
        print(v)
        print(k.split('__'), v)

        """
        Retorna
        name__startswith
        Ama
        ['name', 'startswith'] Ama
        age__lt
        46
        ['age', 'lt'] 46
        city__endswith
        nde
        ['city', 'endswith'] nde
        """

filter(name__startswith='Ama', age__lt=46, city__endswith='nde')


def ak(*args, **kwargs):
    print(args, kwargs)

    """
    Retorna
    ('A', 'B', 'C') {'z': 'Z', 'w': 'W'}
    """


t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

ak(*t, **d)


def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def calc(op, a, b):
    """ Verifica quem é op e chama a função correspondente """
    return op(a, b)


print(calc(add, 2, 3))  # retorna 5
print(calc(mul, 2, 3))  # retorna 6
