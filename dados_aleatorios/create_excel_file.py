import pandas as pd


data_all = pd.read_json("inventores_e_cientistas_famosos.json")
data_all.to_excel("nomes.xlsx", index=False)
