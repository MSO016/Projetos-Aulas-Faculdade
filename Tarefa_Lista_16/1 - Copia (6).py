valores = []
for i in range(10):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

print(f"O maior valor do vetor é: {maior}")
print(f"O menor valor do vetor é: {menor}")
