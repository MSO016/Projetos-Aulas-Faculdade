gabarito = []
print("Digite o gabarito de respostas:")
for i in range(10):
    resposta = input(f"Questão {i+1}: ").strip().lower()
    gabarito.append(resposta)

alunos = []
for i in range(3):
    aluno = {}
    aluno['matricula'] = int(input(f"Digite a matrícula do aluno {i+1}: "))
    aluno['respostas'] = []
    print(f"Digite as respostas do aluno {i+1}:")
    for j in range(10):
        resposta = input(f"Questão {j+1}: ").strip().lower()
        aluno['respostas'].append(resposta)
    alunos.append(aluno)

for aluno in alunos:
    aluno['nota'] = sum(1 for i in range(10) if aluno['respostas'][i] == gabarito[i])

aprovados = sum(1 for aluno in alunos if aluno['nota'] >= 7)
percentual_aprovacao = (aprovados / len(alunos)) * 100


for aluno in alunos:
    print(f"\nMatrícula: {aluno['matricula']}")
    print(f"Respostas: {aluno['respostas']}")
    print(f"Nota: {aluno['nota']}")

print(f"\nPercentual de aprovação: {percentual_aprovacao:.2f}%")
