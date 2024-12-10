from random import randint, sample
import logging
import time
from functools import wraps


logging.basicConfig(
    filename='logs_tabuada.log',
    format='%(asctime)s  %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG
)


def timethis(func):
    """
    Decorador que informa o tempo de execução
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end)
        print(func.__name__, round(end - start, 2))
        print(end)
        return result
    return wrapper


@timethis
def tabuada_aleatoria(nome, numero):
    erros = 0
    acertos = 0
    print(f"\n***** Tabuada Aleatória do {numero} *****\n")
    lista = list(range(1, 11))
    for _ in range(5):
        numero2 = sample(lista, 1)[0]
        correta = numero * numero2
        resposta = int(input(f"{numero} x {numero2} = "))
        lista.remove(numero2)
        if resposta == correta:
            print("Resposta correta\n")
            acertos += 1
        else:
            print(f"Não é bem isso. A resposta correta é {correta}")
            erros += 1
    print(f"\nVocê teve:\n{acertos} acertos\n{erros} erros")
    logging.info(f"Tabuada aleatória do {numero} - {nome} teve {acertos} acertos e {erros} erros")


@timethis
def tabuadas(nome, numero):
    erros = 0
    acertos = 0
    print(f"\n***** Tabuada do {numero} *****\n")
    for num in range(1, 11):
        correta = numero * num
        resposta = int(input(f"{numero} x {num} = "))
        if resposta == correta:
            print("Resposta correta\n")
            acertos += 1
        else:
            print(f"Não é bem isso. A resposta correta é {correta}")
            erros += 1
    print(f"\nVocê teve:\n{acertos} acertos\n{erros} erros")
    logging.info(f"Tabuada do {numero} - {nome} teve {acertos} acertos e {erros} erros")
    tabuada_aleatoria(nome, numero)


print("Responda as questões abaixo:")
nome = input("Digite seu nome: ")
uma_ou_todas = input("Quer fazer todas as tabuadas na ordem? (s ou n): ")

if uma_ou_todas == 'n':
    escolha = int(input("Qual número para a tabuada?: "))
    tabuadas(nome, escolha)
else:
    for tabuada in range(1, 11):
        print(f"Tabuada do {tabuada}")
        tabuadas(nome, tabuada)
