valor1 = int(
    10
)

valor2= 20
valor3=30

if valor1 < valor2:
    print("Valor1 é menor")
    valor1 = valor2
    valor2 = valor1
    # valor1, valor2 = valor2, valor1
    print("Trocando os valores...")
    print(f"Valor1 = {valor1} e Valor2 = {valor2}")
    if valor1 > valor2:
        print("Valor1 é maior")
    else:
        print("Valor2 é maior")
else:
    print("Valor2 é maior")

