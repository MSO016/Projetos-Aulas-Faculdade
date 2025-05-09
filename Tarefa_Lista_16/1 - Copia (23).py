A = []
print("Digite os valores para o vetor A:")
for i in range(5):
    valor = float(input(f"Posição {i}: "))
    A.append(valor)

B = []
print("Digite os valores para o vetor B:")
for i in range(5):
    valor = float(input(f"Posição {i}: "))
    B.append(valor)

produto_escalar = sum(A[i] * B[i] for i in range(5))

print("Vetor A:", A)
print("Vetor B:", B)
print(f"O produto escalar é: {produto_escalar}")
