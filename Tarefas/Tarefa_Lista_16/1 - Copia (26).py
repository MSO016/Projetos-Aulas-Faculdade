import math

valores = []
for i in range(10):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

media = sum(valores) / len(valores)

soma_dos_quadrados = sum((valor - media) ** 2 for valor in valores)
desvio_padrao = math.sqrt(soma_dos_quadrados / (len(valores) - 1))

print(f"A média do vetor é: {media}")
print(f"O desvio padrão do vetor é: {desvio_padrao}")
