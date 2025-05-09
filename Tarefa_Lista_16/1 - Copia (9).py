valores = []
while len(valores) < 6:
    valor = int(input(f"Digite um valor par para a posição {len(valores)}: "))
    if valor % 2 == 0:
        valores.append(valor)
    else:
        print("O valor digitado não é par. Tente novamente.")

print("Os valores pares na ordem inversa são:")
for valor in reversed(valores):
    print(valor)
