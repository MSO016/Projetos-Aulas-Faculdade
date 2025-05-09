A = []
B = []

print("Digite os valores para o vetor A:")
for i in range(10):
    valor = int(input(f"Posição {i}: "))
    A.append(valor)

print("Digite os valores para o vetor B:")
for i in range(10):
    valor = int(input(f"Posição {i}: "))
    B.append(valor)

C = [A[i] - B[i] for i in range(10)]

print("Vetor C (A - B):")
for valor in C:
    print(valor)

