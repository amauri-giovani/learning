import json


filename = 'previsao.txt'

with open(filename, encoding='ISO-8859-1') as f:
    text = f.readlines()

lista = []

for line in text:
    dic = {}
    item = line.split(' _ ')
    # print(item)
    dic['valor'] = item[0].strip()
    dic['modelo'] = item[1].strip()
    dic['ip'] = item[2].strip()
    dic['variavel'] = item[3].strip()
    dic['local_instalação'] = item[4].strip()
    lista.append(dic)


# json = json.dumps(lista)
# print(json)

