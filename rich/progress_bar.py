# https://github.com/ikatyang/emoji-cheat-sheet


from rich.progress import track
from time import sleep


for tarefa in track(range(10), 'Processando...'):
    sleep(1)
