valor1 = int(

    10
)
print(f'valor1: {valor1}')

valor2= 20
print(f'valor2: {valor2}')

valor3=30
print(f'valor3: {valor3}')


if valor1 < valor2:
    print("Valor1 é menor")
    valor1 = valor2
    print(f'valor1: {valor1}')

    valor2 = valor1
    print(f'valor2: {valor2}')

    print("Trocando os valores...")
    if valor1 > valor2:
        print("Valor1 é maior")
    else:
        print("Valor2 é maior")
else:
    print("Valor2 é maior")

