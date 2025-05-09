# Faça um programa que leia do usuário o valor de N.

# Em seguida, calcule a SOMATÓRIO dos números entre 1 a N.

# Mostre o resultado.
N = int(input("Digite um valor para N: "))

for i in range(1, N):
    N += i
print(f"A soma dos números de 1 a N é: {N}")