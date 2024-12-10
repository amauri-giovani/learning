import pandas as pd


filename = r'/home/amauri/Downloads/airports.airport.csv'

texto = pd.read_csv(filename, encoding='utf-8', sep=';')
# texto = pd.read_csv(filename, encoding='ISO-8859-1', sep=';')
# print(texto)
texto.to_json(r'/tmp/airports_json.json')
