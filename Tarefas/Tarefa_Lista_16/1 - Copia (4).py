vetor = []
for i in range(8):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    vetor.append(valor)

X = int(input("Digite a posição X (0 a 7): "))
Y = int(input("Digite a posição Y (0 a 7): "))

soma = vetor[X] + vetor[Y]

print(f"A soma dos valores nas posições {X} e {Y} é: {soma}")
