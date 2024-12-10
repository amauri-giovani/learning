import json

filename = '/home/amauri/tour_house/Arquivos/Rocket/hotel.json'

with open(filename) as f:
    versions = json.load(f)

versions_list = [i['fields'] for i in versions if i['fields']['provider'] == 1]
print()