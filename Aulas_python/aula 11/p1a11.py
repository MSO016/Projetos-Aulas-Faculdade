from math import sqrt

n=int(input("Digite o valor de N: "))

produtorioN= 1
for i in range (1, n+1):
    produtorioN *=i

resultado= (produtorioN **2 / sqrt(produtorioN))
print(f"O resultado é: {resultado}")
