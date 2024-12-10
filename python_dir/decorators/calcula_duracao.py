import time
from functools import wraps

"""
Além de preservar o nome da função, @wraps também copia outras informações importantes da 
função original, como a docstring e as anotações de tipo.
Se você usar o decorador @wraps, o nome da função decorada será o mesmo nome da função original.
Sem usar @wraps, o nome da função decorada é "wrapper"
"""

def tempo_de_execucao(funcao_original):
    @wraps(funcao_original)
    def wrapper():
        inicio = time.time()
        resultado = funcao_original()
        fim = time.time()
        print(funcao_original.__name__)
        print(f"Tempo de execução: {fim - inicio} segundos.")
        return resultado
    return wrapper


@tempo_de_execucao
def minha_funcao():
    for i in range(10):
        print(i + 1)
        time.sleep(0.2)


minha_funcao()
print(minha_funcao.__name__)
