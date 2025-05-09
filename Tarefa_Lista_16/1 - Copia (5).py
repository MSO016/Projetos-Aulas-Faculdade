valores = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

pares = [valor for valor in valores if valor % 2 == 0]

print(f"O vetor possui {len(pares)} valores pares.")
