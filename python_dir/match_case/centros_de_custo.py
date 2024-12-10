from functools import reduce
import logging

def contas(centros):
    match centros:
        case [area, centros]:   # Apenas 1 centro de custo
            print(f"A área {area} possui o centro de custo {centros}")
        case [area, *centros]:   # Com 2 ou mais centros de custo
            print(f"A área {area} possui os centros de custo abaixo:")
            for centro in centros:
                print(centro)


contas(["Financeiro", "ABC"])
contas(["Marketing", "ABC", "XYZ", "HJG"])


def contas2(centros):
    match centros:
        case [*centros]:  # Com 2 ou mais centros de custo
            print(f"{centros} é uma lista")
            for centro in centros:
                print(f"Centro de custo: {centro}")
        case centros:  # Apenas 1 centro de custo
            print(f"{centros} não é lista e sim uma string")


print("*" * 30)
contas2("Financeiro")
contas2(["Marketing", "RH"])


# Apenas estudando a possibilidade
def roles(role):
    permissions = ["read", "write", "download", "premium suport", "admin privileges"]
    nivel = 0
    match role:
        case "admin":
         nivel = len(permissions)
        case "vip":
         nivel = len(permissions) -1
        case "premium":
         nivel = len(permissions) -2
        case "plus":
         nivel = len(permissions) -3
        case "free":
         nivel = len(permissions) -4
    return permissions[:nivel]

role = 'vip'
roles(role)

levels = {
    1: 'read',
    2: 'write',
    3: 'download',
    4: 'premium suport',
    5: 'admin privileges',
}
