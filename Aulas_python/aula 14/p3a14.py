#SEM APPEND
# Crie um programa em Python que crie um vetor (lista) de 5 posições.
# O programa deve pedir ao usuário para digitar um valor para cada posição do vetor, atribuindo o valor diretamente no vetor.
# Em seguida, o programa deve exibir todos os valores do vetor utilizando um laço de repetição.

# Cria o vetor (lista) de 5 posições
vetor = [0] * 5

# Preenche cada posição do vetor com um valor informado pelo usuário
for i in range(5):
    vetor[i] = int(input("Qual valor? "))

# Exibe os valores do vetor
print("Valores do vetor:")
for valor in vetor:
    print(valor)