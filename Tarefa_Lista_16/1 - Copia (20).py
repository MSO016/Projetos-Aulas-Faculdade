valores = []
for i in range(10):
    while True:
        valor = int(input(f"Digite um valor entre 0 e 50 para a posição {i}: "))
        if 0 <= valor <= 50:
            valores.append(valor)
            break
        else:
            print("Valor fora do intervalo. Tente novamente.")

impares = [valor for valor in valores if valor % 2 != 0]

print("Vetor original:")
for i in range(0, len(valores), 2):
    print(valores[i:i+2])

print("\nVetor de ímpares:")
for i in range(0, len(impares), 2):
    print(impares[i:i+2])
