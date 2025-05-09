# Exercício: Soma dos Elementos de um Vetor
#
# Enunciado:
# Crie um programa em Python que crie um vetor (lista) de 5 números inteiros.
# O programa deve calcular e exibir a soma de todos os elementos do vetor.

# Cria o vetor (lista) com 5 números
vetor = []

#inicializa a variável para soma
soma=0
# Solicita que o usuário preencha cada posição do vetor
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    soma = soma + numero

# Exibe a soma
print(f"A soma dos elementos do vetor é: {soma}")