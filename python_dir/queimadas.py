import requests
from pprint import pprint

url_base = "http://queimadas.dgi.inpe.br/queimadas/dados-abertos/api"
estados_municipios = {}

def get_focos_pais(pais_id):
    resp_json = requests.get(f"{url_base}/focos/?pais_id={pais_id}").json()

    for i in resp_json:
        estado = i['properties']['estado']
        municipio = i['properties']['municipio']
        if not estado in estados_municipios:
            estados_municipios[estado] = []
        if not municipio in estados_municipios[estado]:
            estados_municipios[estado].append(municipio)

    return estados_municipios

pprint(get_focos_pais(33))
