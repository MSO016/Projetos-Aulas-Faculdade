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

C = list(set(A + B))

print("Vetor C (união de A e B):")
for valor in C:
    print(valor)
