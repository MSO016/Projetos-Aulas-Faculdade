# Crie um programa que
# solicite ao usuário o número de linhas da matriz
# solicite ao usuário o número de colunas de uma matriz,
# um FOR dentro do outro FOR e leia os elementos da matriz
# solicite um número X do usuário
# com um FOR, multiplique todos os elementos da matriz pelo valor de X
# um outro FOR para mostrar a matriz formatada.
# Crie um programa que solicite ao usuário o número de linhas e colunas de uma matriz, leia os elementos da matriz e imprima a matriz formatada.


# Solicita as dimensões da matriz
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

# Solicita o valor para multiplicar
X = int(input("Digite o valor para multiplicar: "))

# Multiplica a matriz pelo valor
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] *= X

# Imprime a matriz resultante
print("Matriz resultante:")
for linha in matriz:
    print(linha)