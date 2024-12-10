import time


# Define nosso decorator
from functools import wraps


def calcula_duracao(funcao):
    @wraps(funcao)
    def wrappper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        funcao = funcao.__name__
        tempo_total = str(tempo_final - tempo_inicial)
        print(f"[{funcao}] Tempo total de execucao: {tempo_total}")

    return wrappper


@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

main()
