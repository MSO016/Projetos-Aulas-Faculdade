# Crie um programa em Python que crie um vetor (lista) de 10 números inteiros.
# O programa deve calcular a média dos valores no vetor e, em seguida, contar e exibir quantos valores estão acima da média.


# Cria o vetor (lista) vazio
vetor = []

# Solicita que o usuário preencha cada posição do vetor
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# Calcula a média dos valores no vetor
media = sum(vetor) / len(vetor)

# Conta a quantidade de valores acima da média
valores_acima = 0
for valor in vetor:
    if valor > media:
        valores_acima += 1

# Exibe a média e a quantidade de valores acima da média
print(f"A média dos valores é: {media:.1f}")
print(f"Quantidade de valores acima da média: {valores_acima}")