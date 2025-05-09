alunos = []
for i in range(10):
    numero = int(input(f"Digite o número do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} em metros: "))
    alunos.append((numero, altura))

mais_baixo = min(alunos, key=lambda x: x[1])
mais_alto = max(alunos, key=lambda x: x[1])

print(f"O aluno mais baixo é o número {mais_baixo[0]} com altura de {mais_baixo[1]} metros.")
print(f"O aluno mais alto é o número {mais_alto[0]} com altura de {mais_alto[1]} metros.")
