vetorA = []
vetorB = []

print("Digite 10 nomes:")
for i in range(10):
    nome = input(f"Nome {i+1}: ")
    vetorA.append(nome)

print("Digite 10 sobrenomes:")
for i in range(10):
    sobrenome = input(f"Sobrenome {i+1}: ")
    vetorB.append(sobrenome)

print("\nNomes completos:")
for i in range(10):
    print(f"{vetorA[i]} {vetorB[i]}")
