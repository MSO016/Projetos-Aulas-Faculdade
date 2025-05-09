
respostas = []
for i in range(5):
    linha = []
    print(f"Digite as respostas do aluno {i+1}:")
    for j in range(10):
        resposta = input(f"Questão {j+1}: ").strip().lower()
        linha.append(resposta)
    respostas.append(linha)


gabarito = []
print("Digite o gabarito de respostas:")
for j in range(10):
    resposta = input(f"Questão {j+1}: ").strip().lower()
    gabarito.append(resposta)


resultado = []
for i in range(5):
    pontuacao = 0
    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            pontuacao += 1
    resultado.append(pontuacao)


print("Pontuação dos alunos:")
for i in range(5):
    print(f"Aluno {i+1}: {resultado[i]} pontos")
