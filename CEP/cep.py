import requests
from pprint import pprint


cep = input("CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json"
endereco = requests.get(url).json()
# pprint(endereco)
logradouro = endereco['logradouro']
localidade = endereco['localidade']
bairro = endereco['bairro']
uf = endereco['uf']
print(logradouro, localidade, bairro, uf)
