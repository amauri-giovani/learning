import pandas as pd

texto = pd.read_xml('/home/amauri/Downloads/PS195.xml', encoding='ISO-8859-1')
texto = texto.fillna('')
dic = texto.to_dict(orient='records')
# texto = pd.read_html('/home/amauri/Downloads/PS195.htm')
# df = pd.DataFrame(dic)
texto.to_excel('/home/amauri/Downloads/PS195.xlsx')
# print(dic)