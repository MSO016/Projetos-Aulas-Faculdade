tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []
for i in range(tamanho):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    vetor.append(valor)

print(f"Vetor gerado: {vetor}")

for i in range(tamanho):
    if vetor[i] < 0:
        vetor[i] = 0

print(f"Vetor atualizado (valores negativos substituídos por 0): {vetor}")
