matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

# Calcular a transposta da matriz
transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]

print("Matriz original:")
for linha in matriz:
    print(linha)

print("Matriz transposta:")
for linha in transposta:
    print(linha)
