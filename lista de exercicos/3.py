notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("As notas digitadas foram:")
for nota in notas:
    print(nota)

print(f"A média é: {media:.2f}")