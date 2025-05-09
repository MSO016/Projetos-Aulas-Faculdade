# Criar programa que leia do usuário o valor de N e o valor de P.

# Depois calcula a somatória de N e a somatória de P.

# Em seguida, calcule raiz quadrada da somatória de N dividido pela raiz quadrada da somatória de P

# Mostre o resultado
import math

N = int(input("Digite um valor para N: "))
P = int(input("Digite um valor para P: "))

soma_N = 0
soma_P = 0

for i in range(1, N+1):
    soma_N += i

for i in range(1, P+1):
    soma_P += i

raiz_N= math.sqrt (soma_N)
raiz_P= math.sqrt (soma_P)

R= raiz_N/raiz_P

print(f"A divisão dos números de N e P é: {R:.2f}")