valores = []
for i in range(6):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Números pares digitados:", pares)
print("Soma dos números pares digitados:", sum(pares))
print("Números ímpares digitados:", impares)
print("Quantidade de números ímpares digitados:", len(impares))
