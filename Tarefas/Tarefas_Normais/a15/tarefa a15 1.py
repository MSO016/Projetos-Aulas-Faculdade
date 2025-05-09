notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

somatoria = 0
for nota in notas:
    somatoria += nota

media = somatoria / 10

print(f"A média das notas é: {media:.2f}")