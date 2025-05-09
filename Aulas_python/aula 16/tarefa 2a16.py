# Crie um programa que solicite ao usuário o número de linhas e colunas de uma matriz, leia os elementos da matriz e imprima a matriz formatada.

# Solicita o número de linhas e colunas da matriz
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

# Cria a matriz
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Imprime a matriz formatada
for linha in matriz:
    print(linha)