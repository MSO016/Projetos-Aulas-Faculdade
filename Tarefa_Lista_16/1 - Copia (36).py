valores = []
for i in range(10):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

valores_ordenados = sorted(valores)

print("Vetor ordenado:")
for valor in valores_ordenados:
    print(valor)
