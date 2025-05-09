
notas = []
for i in range(10):
    linha = []
    print(f"Digite as notas do aluno {i+1}:")
    for j in range(3):
        nota = float(input(f"Nota da prova {j+1}: "))
        linha.append(nota)
    notas.append(linha)

pior_nota_prova1 = 0
pior_nota_prova2 = 0
pior_nota_prova3 = 0

for i in range(10):
    piores_notas = sorted([(notas[i][0], 1), (notas[i][1], 2), (notas[i][2], 3)])
    pior_prova = piores_notas[0][1]
    if pior_prova == 1:
        pior_nota_prova1 += 1
    elif pior_prova == 2:
        pior_nota_prova2 += 1
    else:
        pior_nota_prova3 += 1


print(f"Número de alunos cuja pior nota foi na prova 1: {pior_nota_prova1}")
print(f"Número de alunos cuja pior nota foi na prova 2: {pior_nota_prova2}")
print(f"Número de alunos cuja pior nota foi na prova 3: {pior_nota_prova3}")