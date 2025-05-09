numeros = []
for i in range(10):
    valor = float(input(f"Digite o número {i+1}: "))
    numeros.append(valor)

quadrados = [x**2 for x in numeros]

print("Conjunto de números reais:")
for numero in numeros:
    print(numero)

print("\nConjunto dos quadrados:")
for quadrado in quadrados:
    print(quadrado)
