import json
from pprint import pprint

import xmltodict

arquivo = "SessionCreateRQ.json"

with open(arquivo) as f:
    text = f.read()

conv_json = json.loads(text)
pprint(conv_json)



# dic = json.dumps(xmltodict.parse(text), indent=4)
# print("type ==>", type(xml_convertido))
# print("xml_convertido ==>", xml_convertido)

# json_dict = json.dumps(xmltodict.parse(text), indent=4)
# print("type ==>", type(json_dict))
# print("json_dict ==>", json_dict)

# desconvertido = xmltodict.unparse(json.loads(dic), pretty=True)
# print("type ==>", type(desconvertido))
# print("desconvertido ==>", desconvertido)
