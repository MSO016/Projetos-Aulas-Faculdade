valores = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

v1 = [valor for valor in valores if valor % 2 != 0]
v2 = [valor for valor in valores if valor % 2 == 0]

print("Elementos utilizados de v1 (ímpares):")
for valor in v1:
    print(valor)

print("\nElementos utilizados de v2 (pares):")
for valor in v2:
    print(valor)
