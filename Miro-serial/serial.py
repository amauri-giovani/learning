from random import randint



matriz = [[1, 0, 1, 0, 1, 1, 1, 0]]


def gera_lista():
    novos_dados = []
    for i in range(8):
        novos_dados.append(randint(0, 1))
    # matriz.append(novos_dados)
    return novos_dados


def compara(x, y):
    if not x == y:
        matriz.append(x)
        print(False)
    else:
        print(True)
    print("MATRIZ ===>", matriz)


print("MATRIZ = ", matriz)


a = gera_lista()
print("a", a)
print(matriz[-1])
print("MATRIZ = ", matriz)
compara(a, matriz[-1])
print()

b = gera_lista()
print("b", b)
print(matriz[-1])
print("MATRIZ = ", matriz)
compara(b, matriz[-1])
print()

c = gera_lista()
print("c", c)
print(matriz[-1])
print("MATRIZ = ", matriz)
compara(c, matriz[-1])
print()

d = gera_lista()
print("d", d)
print(matriz[-1])
print("MATRIZ = ", matriz)
compara(d, matriz[-1])
print()

e = gera_lista()
print("e", e)
compara(e, matriz[-1])
print("MATRIZ = ", matriz)
print()


# print("MATRIZ = ", matriz)