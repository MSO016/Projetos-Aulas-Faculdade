valores = []
while len(valores) < 10:
    valor = int(input(f"Digite um valor diferente para a posição {len(valores)}: "))
    if valor in valores:
        print("Valor já digitado anteriormente. Por favor, digite outro número.")
    else:
        valores.append(valor)

print("Vetor final:")
for valor in valores:
    print(valor)
