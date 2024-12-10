import os
from sys import stdout
from time import sleep


def download_status(dirname):
    os.chdir(dirname)
    count = 0
    while True:
        if not os.listdir(dirname) and count < 11:
            stdout.write(f'\rAguardando início do download: {count}s')
            stdout.flush()
            sleep(1)
            count += 1
        elif count == 11:
            print(f'\nNenhum arquivo foi encontrado para download')
            return False
        else:
            print('\nArquivo encontrado')
            break

    count = 0

    while True:
        if os.listdir(dirname)[0].endswith(".crdownload"):
            sleep(1)
            count += 1
            stdout.write(f'\rDownload em andamento')
            stdout.flush()
        else:
            stdout.write(f'\rDownload concluído')
            stdout.flush()
            break

dirname = '/home/amauri/tour_house/Arquivos/SLA/bots_argo/processing'
download_status(dirname)
