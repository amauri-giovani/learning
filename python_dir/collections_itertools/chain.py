from itertools import chain

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
d = a + b + c

# print(d)
# print(sum([a, b, c], []))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

result = chain(a, b, c)
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# <itertools.chain object at 0x7f660bb1c8b0>
# 1
# 2
# 3
# 4
# for x in result:
#     print(x)
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# print(list(result))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def _chain(*iters):
    for l in iters:
        yield from l

# print(list(_chain([1, 2, 3, 4], [5, 6, 7, 8])))
# [1, 2, 3, 4, 5, 6, 7, 8]
