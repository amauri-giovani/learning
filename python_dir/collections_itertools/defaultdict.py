from collections import defaultdict


# defaultdict
# ===========
# Não retorna KeyError, constrói {chave: valor}
def none():
    return None


d = defaultdict(none)
d['css']
# print(d)
# defaultdict(<function none at 0x7fe7f436d940>, {'css': None})

d2 = defaultdict(lambda: 7)
d2['oi']
# print(d2)
# defaultdict(<function <lambda> at 0x7f98c7d2e940>, {'oi': 7})


counts = defaultdict(int)
for _ in range(int(input())):
    counts[input()] += 1

print(len(counts))
print(*counts.values())
