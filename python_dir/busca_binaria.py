import json

from python_dir.stopwatch import stopwatch

with open('orders.json') as file_obj:
    list_orders = json.load(file_obj)

dic = {k: k for k in list_orders}


@stopwatch
def busca_binaria(lista, item, cont=0):
    print(item, cont)
    cont += 1
    meio = len(lista) // 2
    if item > lista[meio]:
        busca_binaria(lista[meio:], item, cont)
    elif item < lista[meio]:
        busca_binaria(lista[:meio], item, cont)
    elif item == lista[meio]:
        return True
    return False


@stopwatch
def busca_for(lista, item, cont=0):
    for i in lista:
        cont += 1
        if i == item:
            return True
    return True


@stopwatch
def busca_dict(item):
    dic = {k: k for k in list_orders}
    return item in dic


@stopwatch
def busca_dict_pronto(item):
    return item in dic


@stopwatch
def busca_in(lista, item):
    return item in lista


busca_binaria(list_orders, 46398, 0)
# print(resp_binaria)
# print()

busca_for(list_orders, 46398)
# print(resp_busca_for)
# print()

busca_dict(46398)
# print(resp_busca_dict)

busca_dict_pronto(46398)
# print(resp_busca_dict_pronto)

busca_in(list_orders, 46398)
# print(resp_busca_in)
