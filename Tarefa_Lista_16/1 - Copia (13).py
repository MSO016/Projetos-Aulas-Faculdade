valores = []
for i in range(5):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)
posicao_maior = valores.index(maior)
posicao_menor = valores.index(menor)

print("Valores lidos:", valores)
print(f"O maior valor é: {maior}, na posição {posicao_maior}")
print(f"O menor valor é: {menor}, na posição {posicao_menor}")
