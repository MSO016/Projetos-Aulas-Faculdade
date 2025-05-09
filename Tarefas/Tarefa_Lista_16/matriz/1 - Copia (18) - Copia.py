matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)


soma_colunas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]


print("Matriz:")
for linha in matriz:
    print(linha)

print("Array unidimensional (soma das colunas):")
print(soma_colunas)