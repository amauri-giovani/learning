from sys import stdout
from time import sleep


def save_action(action) -> None:
    # print(f"\r{action}", end=" " * (len(lista[i]) - 1), flush=True)
    # print(" ", end=s)
    # s = stdout.write(f'\r{action}')
    stdout.write(f'\r{" " * 100}')
    stdout.flush()
    stdout.write(f'\r{action} ')
    stdout.flush()
    # print(f"\r{action}", end=" " * 5, flush=True)


lista = ["Os links foram trocados",
         "Entrou na página de relatórios",
         "Relatorio de SLA Processado em 11/fev/2023 03:08. Relatorio disponível para download.",
         "(Última Atualização antes do processamento:: 11/02/2023 03:08:09)",
         "Clicando no link para download",
         "Aguardando alert",
         "Clicando em alert"
         ]

for i, frase in enumerate(lista):
    save_action(frase)
    sleep(0.5)
