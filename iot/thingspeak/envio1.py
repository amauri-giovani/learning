'''
Envio de informações para o site ThingSpeak
Usado o exemplo do vídeo: https://www.youtube.com/watch?v=zQEGr0ItRQ4

Em API Keys foi utilizada a url:
https://api.thingspeak.com/update?api_key=DXTUHWTZUYHYE3EL&field1=0
'''

import urllib3

url_base = "https://api.thingspeak.com/update"
api_key = "api_key=DXTUHWTZUYHYE3EL"
field = "field1"
valor_field = "9.13"

urllib3.PoolManager().request("GET", f"{url_base}?{api_key}&{field}={valor_field}")
