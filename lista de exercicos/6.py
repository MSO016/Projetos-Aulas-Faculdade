notas = []
media_alunos = []

for i in range(10):
    aluno_notas = []
    print(f"\nAluno {i+1}:")
    
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        aluno_notas.append(nota)
    
    media = sum(aluno_notas) / 4
    media_alunos.append(media)

alunos_aprovados = sum(1 for media in media_alunos if media >= 7.0)

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}")