"""
Envio de informações para o ThingSpeak
URL para visualização: https://thingspeak.com/channels/1361670
Necessário ter o arquivo ".env" que possui a API Keys
"""

from random import randint
from time import sleep
from requests import get
from decouple import config


url_base = "https://api.thingspeak.com/update"
api_key = config("api_key")


def envia_informacao(field: int, valor: int) -> None:
    get(f"{url_base}?api_key={api_key}&field{field}={valor}")
    return None


while True:
    field = 1
    valor = randint(0, 100)
    envia_informacao(field, valor)
    print(f"Valor enviado: {valor}")
    sleep(10)
