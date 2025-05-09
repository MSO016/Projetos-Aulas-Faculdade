caracteres = []
consoantes = []

print("Digite 10 caracteres:")
for _ in range(10):
    caractere = input().lower()
    caracteres.append(caractere)
    if caractere.isalpha() and caractere not in 'aeiou':
        consoantes.append(caractere)

print(f"\nForam lidas {len(consoantes)} consoantes:")
print(" ".join(consoantes))
