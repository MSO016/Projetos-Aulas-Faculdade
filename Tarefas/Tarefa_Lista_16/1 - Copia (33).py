valores = []
for i in range(15):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

# Compactar o vetor eliminando os valores zero
valores_compactados = [valor for valor in valores if valor != 0]

print("Vetor compactado:")
for valor in valores_compactados:
    print(valor)
