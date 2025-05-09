#Crie um programa que leia do usuário um vetor de 10 elementos.

#Depois, calcule o produtório dos elementos do vetor.

vetor= [0] * 10
produtorio= 1
for i in range(10):
    n=int(input(f"Digite o {i+1}º número: "))
    produtorio= produtorio * n
print(f"o valor do produtorio é: {produtorio}")