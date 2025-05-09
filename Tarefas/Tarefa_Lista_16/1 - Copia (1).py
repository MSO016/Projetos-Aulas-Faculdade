A = []
for i in range(6):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    A.append(valor)

soma = A[0] + A[1] + A[5]
print("A soma dos valores nas posições A[0], A[1] e A[5] é:", soma)

A[4] = 100

for valor in A:
    print(valor)
