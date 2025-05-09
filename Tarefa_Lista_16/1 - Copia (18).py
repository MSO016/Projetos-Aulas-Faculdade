valores = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

x = int(input("Digite um número inteiro x: "))

multiplos = [valor for valor in valores if valor % x == 0]

print(f"Os múltiplos de {x} no vetor são: {multiplos}")
print(f"Quantidade de múltiplos de {x}: {len(multiplos)}")
