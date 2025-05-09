# Leia do usuário o TAMANHO do vetor

# Utilize o FOR e o RAND para inserir valores aleatórios em cada posição do vetor

# Faça outro FOR e mostre o vetor gerado

import random

tamanho= int(input("digite o tamanho do vetor: "))
vetor= [random.radint(1, 100) for _ in range (tamanho)]

print("vetor gerado")
for valor in vetor:
    print(valor)