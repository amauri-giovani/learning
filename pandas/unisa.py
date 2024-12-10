import pandas as pd

filename = '/home/amauri/Clarice/canc.csv'

# texto = pd.read_csv(filename, encoding='utf-8', sep=';')
texto = pd.read_csv(filename, encoding='ISO-8859-1', sep=';')
# print(texto)

df = pd.DataFrame(texto)
df.to_excel('/home/amauri/Clarice/cancelados.xlsx')

