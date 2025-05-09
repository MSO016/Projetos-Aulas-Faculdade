import random

def gerar_cartela():
    numeros = random.sample(range(100), 25)
    cartela = [numeros[i:i+5] for i in range(0, 25, 5)]
    return cartela

def imprimir_cartela(cartela):
    for linha in cartela:
        print(" ".join(f"{num:2d}" for num in linha))

cartela = gerar_cartela()

print("Cartela de Bingo gerada:")
imprimir_cartela(cartela)
