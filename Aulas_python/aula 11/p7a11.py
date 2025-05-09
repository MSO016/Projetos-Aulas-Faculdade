# Leia o valor de N do usuário e calcule a somatório de N valores fornecidos decimais pelo usuário

# Leia o valor de M do usuário e calcule o produtório de M valores fornecidos decimais pelo usuário

# Calcule a média ponderada W, onde:
# W = (3 * SomatorioN + 2 * ProdutorioM) / 5

N = int(input("Digite o valor de N: "))
M = int(input("Digite o valor de M: "))

somatorioN = 0
produtorioM = 1

for i in range(N):
    valor1 = float(input('Informe um valor decimal: '))
    somatorioN += valor1

for i in range(M):
    valor = float(input('Informe um valor decimal: '))
    produtorioM *= valor

W = (3 * somatorioN + 2 * produtorioM) / 5

print(f"Este é o resultado do seu N, ou de seus valores: {W}")