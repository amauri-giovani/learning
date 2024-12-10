import pandas as pd
# import matplotlib.pyplot as plt


x = pd.read_excel("users_salesbox.xlsx", sheet_name="Usuarios")


print(x)
# pd.read_excel()
# for unidade in
# iata, titulo = x["Unidade"][2].split(" - ")
# print(iata)
# print(titulo)
# print(x["Unidade"][2])
# print(x.loc[[2]])
#
# print("=" * 50)
# print()
#
# for line in x.loc:
#     print(f"line ===> {line}")

# print(x)
# print(x['Unidade'][2])
# print(x.head())
# print(x.info())

# plt.plot(x["Região"])
# plt.plot(x["População 2010"])
# plt.hist(x["População 2010"], bins=20)
# x = pd.read_excel("Pessoas.xlsx")
# plt.pie(x["Idade"], labels=x["Nome"], autopct="%1.2f%%")
#
# plt.show()
