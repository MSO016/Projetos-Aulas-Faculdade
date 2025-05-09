valores = []
for i in range(20):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

valores_unicos = list(set(valores))

print("Os valores sem repetição são:")
for valor in valores_unicos:
    print(valor)
