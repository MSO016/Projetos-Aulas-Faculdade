# Calcule:
# SK: Somatória dos quadrados dos K números decimais fornecidos pelo usuário. Dica: (SK+= numero*numero)
# PL: Produtório das frações dos L números decimais fornecidos pelo usuário. Dica (PL *= 1/numero)

# Depois calcule:
#  resultado = raiz(SK)/ raiz(PL)

# Mostre o resultado
import math

k = int(input("Digite o valor de K: "))
p = int(input("Digite o valor de P: "))

somatorioK = 0
produtorioP = 1

for i in range(1,k+1):
    numero = float(input('Informe um valor decimal: '))
    somatorioK += numero*numero


for i in range(1,p+1):
    numero1 = float(input('Informe um valor decimal: '))
    produtorioP *= 1/numero1

w = math.sqrt(somatorioK)/ math.sqrt(produtorioP)

print(f"Este é o resultado do seu N, ou de seus valores: {w:.2f}")