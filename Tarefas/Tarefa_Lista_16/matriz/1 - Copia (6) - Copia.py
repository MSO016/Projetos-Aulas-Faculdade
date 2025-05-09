
matriz1 = []
print("Digite os valores para a primeira matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Posição ({i}, {j}): "))
        linha.append(valor)
    matriz1.append(linha)


matriz2 = []
print("Digite os valores para a segunda matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Posição ({i}, {j}): "))
        linha.append(valor)
    matriz2.append(linha)

matriz3 = []
for i in range(4):
    linha = []
    for j in range(4):
        maior_valor = max(matriz1[i][j], matriz2[i][j])
        linha.append(maior_valor)
    matriz3.append(linha)


print("Terceira matriz com os maiores valores de cada posição:")
for linha in matriz3:
    print(linha)
