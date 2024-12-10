l1 = [0, 1, 2, 3]
strings = ['zero', 'um', 'dois', 'três']

# print({chave: valor for chave, valor in zip(l1, strings)})
# {0: 'zero', 1: 'um', 2: 'dois', 3: 'três'}

# print(tuple(zip(l1, strings)))
# ((0, 'zero'), (1, 'um'), (2, 'dois'), (3, 'três'))

head, *_, tail = [0, 1, 2, 3, 4]


# print(head)
# 0
# print(_)
# [1, 2, 3]
# print(tail)
# 4
