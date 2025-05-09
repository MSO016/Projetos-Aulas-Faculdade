def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

valores = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

print("Números primos e suas posições:")
for i, valor in enumerate(valores):
    if eh_primo(valor):
        print(f"Valor: {valor}, Posição: {i}")
