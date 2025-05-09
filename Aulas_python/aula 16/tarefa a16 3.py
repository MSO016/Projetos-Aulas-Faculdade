# Leia do usuário o TAMANHO do vetor

# Utilize o FOR e o RAND para inserir valores aleatórios em cada posição do vetor

# Faça outro FOR e mostre os valores PARES

# Faça outro FOR e mostre os valores IMPARES

import random

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []
for i in range(tamanho):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    vetor.append(valor)

print(f"Vetor gerado: {vetor}")

pares = [num for num in vetor if num % 2 == 0]
print(f"Valores pares: {pares}")

impares = [num for num in vetor if num % 2 != 0]
print(f"Valores ímpares: {impares}")
