
alunos = []

for i in range(5):
    aluno = []
    matricula = int(input(f"Digite o número de matrícula do aluno {i+1}: "))
    media_provas = float(input(f"Digite a média das provas do aluno {i+1}: "))
    media_trabalhos = float(input(f"Digite a média dos trabalhos do aluno {i+1}: "))
    aluno.extend([matricula, media_provas, media_trabalhos])
    alunos.append(aluno)

for aluno in alunos:
    nota_final = aluno[1] + aluno[2]
    aluno.append(nota_final)

maior_nota_final = max(alunos, key=lambda x: x[3])
matricula_maior_nota = maior_nota_final[0]

media_notas_finais = sum(aluno[3] for aluno in alunos) / len(alunos)

print("\nMatrícula do aluno com a maior nota final:", matricula_maior_nota)
print("Média aritmética das notas finais:", media_notas_finais)
