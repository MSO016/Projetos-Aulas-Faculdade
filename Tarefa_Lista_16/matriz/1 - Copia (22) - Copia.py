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

def multiplicar_matrizes(matriz1, matriz2):
    tamanho = len(matriz1)
    matriz_resultado = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            for k in range(tamanho):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz_resultado

print("Digite os valores para a matriz A 3x3:")
matrizA = ler_matriz(3)
print("Digite os valores para a matriz B 3x3:")
matrizB = ler_matriz(3)

matrizC = multiplicar_matrizes(matrizA, matrizB)

print("Matriz A:")
imprimir_matriz(matrizA)
print("Matriz B:")
imprimir_matriz(matrizB)
print("Matriz C (A * B):")
imprimir_matriz(matrizC)
