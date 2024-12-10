"""
Envio de informações para o Twitter através do ThingSpeak
Necessário aguardar 60 segundos entre as mensagens para o Twitter não bloquear
Para garantir que não haja bloqueio, a mensagem possui as palavras embaralhadas
URL para visualização: https://twitter.com/amaurigiovani
Necessário ter o arquivo ".env" que possui a API Keys
"""

import random
from time import sleep
from requests import post
from decouple import config


BASE_URL = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update"
API_KEY = config("api_key")
cont = 0


def envia_informacao(cont) -> None:
    mensagens = ["Aviso de monitoramento", f"Número: {cont}", "Teste", "Faculdade Impacta", "AC4"]
    random.shuffle(mensagens)
    mensagem = (" - ").join(mensagens)
    print(mensagem)
    data = {"api_key": API_KEY, f"status": f"{mensagem}"}
    post(url=BASE_URL, data=data)
    return None


while True:
    valor = random.randint(0, 1)
    print(f"Valor: {valor}")
    if valor == 1:
        cont += 1
        envia_informacao(cont)
        print("ATENÇÃO: Sua casa foi invadida!")
    sleep(60)
