valores = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

maior = max(valores)
posicao_maior = valores.index(maior)

print("Vetor:", valores)
print(f"O maior valor do vetor é: {maior}")
print(f"A posição do maior valor é: {posicao_maior}")
