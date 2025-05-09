vetor1 = []
vetor2 = []
vetor_intercalado = []


for i in range(10):
    num = int(input(f"Digite o {i+1}º elemento do primeiro vetor: "))
    vetor1.append(num)


for i in range(10):
    num = int(input(f"Digite o {i+1}º elemento do segundo vetor: "))
    vetor2.append(num)


for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])

print("\nVetor intercalado:")
print(vetor_intercalado)