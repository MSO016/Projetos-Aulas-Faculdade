def ler_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            valor = float(input(f"Digite o valor para a posição ({i}, {j}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def somar_matrizes(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]

def subtrair_matrizes(matriz1, matriz2):
    return [[matriz1[i][j] - matriz2[i][j] for j in range(2)] for i in range(2)]

def adicionar_constante(matriz, constante):
    return [[matriz[i][j] + constante for j in range(2)] for i in range(2)]

print("Digite os valores para a primeira matriz 2x2:")
matriz1 = ler_matriz(2)
print("Digite os valores para a segunda matriz 2x2:")
matriz2 = ler_matriz(2)

while True:
    print("\nMenu de opções:")
    print("(a) Somar as duas matrizes")
    print("(b) Subtrair a primeira matriz da segunda")
    print("(c) Adicionar uma constante às duas matrizes")
    print("(d) Imprimir as matrizes")
    print("(e) Sair")
    opcao = input("Escolha uma opção: ").strip().lower()

    if opcao == 'a':
        resultado = somar_matrizes(matriz1, matriz2)
        print("Resultado da soma das matrizes:")
        imprimir_matriz(resultado)
    elif opcao == 'b':
        resultado = subtrair_matrizes(matriz1, matriz2)
        print("Resultado da subtração da primeira matriz da segunda:")
        imprimir_matriz(resultado)
    elif opcao == 'c':
        constante = float(input("Digite a constante a ser adicionada: "))
        matriz1 = adicionar_constante(matriz1, constante)
        matriz2 = adicionar_constante(matriz2, constante)
        print("Matrizes após adicionar a constante:")
        print("Primeira matriz:")
        imprimir_matriz(matriz1)
        print("Segunda matriz:")
        imprimir_matriz(matriz2)
    elif opcao == 'd':
        print("Primeira matriz:")
        imprimir_matriz(matriz1)
        print("Segunda matriz:")
        imprimir_matriz(matriz2)
    elif opcao == 'e':
        break
    else:
        print("Opção inválida. Tente novamente.")
