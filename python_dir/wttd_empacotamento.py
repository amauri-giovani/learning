row = 'Amauri', 'Praia Grande', 22.9, 43.1

def f(t):
    """ Tudo que não quero fica em *meio em forma de lista """
    # nome, cidade, lat, long = t
    nome, *meio, long = t
    print(nome, long, meio)

    """
    Retorna
    Amauri 43.1 ['Praia Grande', 22.9]
    """

table = (('Amauri', 'Praia Grande', 22.9, 43.1), ('Leonardo', 'São Paulo', 2.4, 54.7))

for nome, *_ in table:
    print(nome, _)

    """
    Retorna
    Amauri ['Praia Grande', 22.9, 43.1]
    Leonardo ['São Paulo', 2.4, 54.7]
    """

print()


if __name__ == '__main__':
    f(row)
