matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

X = int(input("Digite o valor X a ser buscado na matriz: "))

encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == X:
            print(f"Valor {X} encontrado na posição ({i}, {j}).")
            encontrado = True

if not encontrado:
    print("Valor não encontrado.")
