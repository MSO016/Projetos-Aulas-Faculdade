valores = []
for i in range(10):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

valores = [0 if valor < 0 else valor for valor in valores]

print("Vetor atualizado:")
for valor in valores:
    print(valor)
