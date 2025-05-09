from math import sqrt

n=int(input("Digite o valor de N: "))
p=int(input("Digite o valor de P: "))

somatoriaP= 0
for i in range (1, p+1):
    somatoriaP +=i

produtorioN= 1
for i in range (1, n+1):
    produtorioN *=i

resultado= sqrt(somatoriaP) / sqrt(produtorioN)
print(f"O resultado é: {resultado}")
