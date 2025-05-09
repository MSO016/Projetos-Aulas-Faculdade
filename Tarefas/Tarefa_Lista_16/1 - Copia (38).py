valores = []

for i in range(10):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)
    valores.sort()
    print(f"Valores ordenados até agora: {valores}")

print("Valores finais ordenados:")
for valor in valores:
    print(valor)
