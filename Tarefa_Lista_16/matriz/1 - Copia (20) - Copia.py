# Ler a matriz 3x6
matriz = []
for i in range(3):
    linha = []
    for j in range(6):
        valor = float(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

soma_colunas_impares = sum(matriz[i][j] for i in range(3) for j in range(6) if j % 2 == 0)
print(f"Soma dos elementos das colunas ímpares: {soma_colunas_impares}")

media_segunda_quarta_colunas = (sum(matriz[i][1] for i in range(3)) + sum(matriz[i][3] for i in range(3))) / 6
print(f"Média aritmética dos elementos da segunda e quarta colunas: {media_segunda_quarta_colunas}")


for i in range(3):
    matriz[i][5] = matriz[i][0] + matriz[i][1]


print("Matriz modificada:")
for linha in matriz:
    print(linha)
