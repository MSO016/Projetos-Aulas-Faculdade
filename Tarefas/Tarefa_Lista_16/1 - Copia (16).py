valores = []
for i in range(5):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

codigo = int(input("Digite um código (0 para finalizar, 1 para ordem direta, 2 para ordem inversa): "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    print("Vetor na ordem direta:")
    for valor in valores:
        print(valor)
elif codigo == 2:
    print("Vetor na ordem inversa:")
    for valor in reversed(valores):
        print(valor)
else:
    print("Código inválido.")
