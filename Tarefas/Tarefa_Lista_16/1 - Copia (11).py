valores = []
for i in range(10):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

negativos = [valor for valor in valores if valor < 0]
positivos = [valor for valor in valores if valor >= 0]

print(f"A quantidade de números negativos é: {len(negativos)}")
print(f"A soma dos números positivos é: {sum(positivos)}")
