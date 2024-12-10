from random import randint
from pprint import pprint


dic = {}
ean = 0

def insere_produto(ean):
    if not ean in dic:
        dic[ean] = 1
    else:
        dic[ean] += 1

for i in range(10):
    insere_produto(randint(7890000000000, 7899999999999))

pprint(dic)
print(len(dic))

