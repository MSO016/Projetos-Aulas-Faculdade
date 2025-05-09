nomes = []

print("Digite 10 nomes:")
for _ in range(10):
    nome = input()
    nomes.append(nome)

print("Nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
