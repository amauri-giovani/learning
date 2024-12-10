from time import sleep
from rich.console import Console
from rich import print

console = Console()

# def criar_arquivos():
#     for i in range(10):
#         with open(f'arquivo{i}.txt', 'w') as f:
#             f.write('Criamos um novo arquivo')
#             sleep(1)
#             console.log(f'Tarefa {i} finalizada!')
#
#
# with console.status('[green]Realizando a tarefa...[/]') as fi:
#     criar_arquivos()


def tarefa():
    print(':raised_hand_with_fingers_splayed:')
    lista = []
    for i in range(100000000):
        lista.append(i)
    print(':smiley:')

with console.status('[green]Realizando a tarefa...[/]') as fi:
    tarefa()
