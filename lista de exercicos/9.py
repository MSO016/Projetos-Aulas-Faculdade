A = []
soma_quadrados = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    A.append(num)
    soma_quadrados += num ** 2  # Soma do quadrado do número

print("A soma dos quadrados dos elementos do vetor A é:", soma_quadrados)