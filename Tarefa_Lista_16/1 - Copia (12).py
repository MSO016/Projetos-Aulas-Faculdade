valores = []
for i in range(5):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)
media = sum(valores) / len(valores)

print("Valores lidos:", valores)
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A média dos valores é: {media:.2f}")
