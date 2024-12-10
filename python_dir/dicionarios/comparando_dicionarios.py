from collections import ChainMap
from itertools import groupby
from operator import itemgetter
from pprint import pprint

# ChainMap
# a = {
#     "x": 1,
#     "y": 2,
#     "z": 3
#
# }
#
# b = {
#     "w": 10,
#     "x": 11,
#     "y": 2
# }

# print(a.keys())
# print(b.keys())
# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(a.items() & b.items())

# merged = ChainMap(a, b)
# print(merged)
# >>> ChainMap({'x': 1, 'y': 2, 'z': 3}, {'w': 10, 'x': 11, 'y': 2})

# Fim do ChainMap
# ===================================================================

# Ordenando com itemgetter

# Exemplo 1
# rows = [
#     {"fname": "Brian", "lname": "Jones", "uid": 1003},
#     {"fname": "David", "lname": "Beazley", "uid": 1002},
#     {"fname": "John", "lname": "Cleese", "uid": 1001},
#     {"fname": "Big", "lname": "Jones", "uid": 1004}
# ]
#
# by_fname = sorted(rows, key=itemgetter("fname"))
# by_uid = sorted(rows, key=itemgetter("uid"))
#
# pprint(by_fname)
# pprint(by_uid)

# Fim do Exemplo 1
# ===================================================================

# Exemplo 2
# rows = [
#     {"fname": "Brian", "lname": "Jones", "uid": 1003, "languages": ["python", "Javascript", "C#", "Java"]},
#     {"fname": "David", "lname": "Beazley", "uid": 1002, "languages": ["Java", "python"]},
#     {"fname": "John", "lname": "Cleese", "uid": 1001, "languages": ["Javascript", "C#"]},
#     {"fname": "Big", "lname": "Jones", "uid": 1004, "languages": ["Javascript", "python", "C#"]}
# ]
#
# by_fname = sorted(rows, key=itemgetter("fname"))
# by_uid = sorted(rows, key=itemgetter("uid"))
# by_languages = sorted(rows, key=itemgetter("languages"))
# pprint(by_fname)
# pprint(by_uid)
# pprint(by_languages)

# Fim do Exemplo 2
# ===================================================================

# Exemplo 3
rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003, "Office": "Developer"},
    {"fname": "David", "lname": "Beazley", "uid": 1002, "Office": "Technical"},
    {"fname": "John", "lname": "Cleese", "uid": 1001, "Office": "Technical"},
    {"fname": "Big", "lname": "Jones", "uid": 1004, "Office": "Developer"}
]

by_fname = sorted(rows, key=itemgetter("fname"))
by_uid = sorted(rows, key=itemgetter("uid"))
by_office = sorted(rows, key=itemgetter("Office"))

# pprint(by_fname)
# pprint(by_uid)
pprint(by_office)

office_groups = groupby(by_office, key=itemgetter("Office"))
pprint(office_groups)


# Fim do Exemplo 3
# ===================================================================
