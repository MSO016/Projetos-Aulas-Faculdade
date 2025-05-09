matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

soma_diagonal_secundaria = sum(matriz[i][2-i] for i in range(3))

print("Matriz:")
for linha in matriz:
    print(linha)

print(f"A soma dos elementos na diagonal secundária é: {soma_diagonal_secundaria}")
