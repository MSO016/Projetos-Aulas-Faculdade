#Faça um programa que:
#leia do usuário um vetor de 10 posições.
#mostre o vetor na ordem inversa

vetor = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i+1}: "))
    vetor.append(valor)

print("Vetor na ordem inversa:")
for valor in vetor[::-1]: #[::2]: conta em par e o -1 conta o numero -1, ja no dois ele conta 2 em 2.
    print(valor)

