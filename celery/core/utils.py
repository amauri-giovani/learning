from time import sleep

from celery_basic.models import Arquivo
from core.celery import app


@app.task(name="sum_two_numbers")
def add(x, y):
    sleep(2)
    return x + y


def create_file(nome, arquivo):
    Arquivo.objects.create(
        nome=nome,
        arquivo_upload=arquivo
    )
