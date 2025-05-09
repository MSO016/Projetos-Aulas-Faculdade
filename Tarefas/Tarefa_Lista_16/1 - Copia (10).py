notas = []
for i in range(15):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média geral das notas é: {media:.2f}")
