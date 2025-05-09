# # Faça um programa que leia do usuário o valor de N e o valor de P.
# # Depois, calcule a somatória de N dividida pela somatória de P

# # r = SomatoriaN / somatoriaP

# # Mostre o resultado

N = int(input("Digite um valor para N: "))
P = int(input("Digite um valor para P: "))

soma_N = 0
soma_P = 0

for i in range(1, N):
    soma_N += i

for i in range(1, P):
    soma_P += i

R= soma_N/soma_P
print(f"A divisão dos números de N e P é: {R:.2f}")

# N = int(input("Digite um valor para N: "))
# P = int(input("Digite um valor para P: "))

# soma_N = 0
# soma_P = 0

# for i in range(1, N, P):
#     soma_N += i
#     soma_P += i

# R= soma_N/soma_P
# print(f"A divisão dos números de N e P é: {R:.2f}")
