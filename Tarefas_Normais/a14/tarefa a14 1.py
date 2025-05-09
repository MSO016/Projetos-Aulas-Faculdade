print("Exemplo do While: ")

contador = 5
while contador >= 0:
    print(contador)
    contador -= 1

print("Exemplo do For:")

for contador in range(5, -1, -1): #vc define onde começa(5), onde termina(-1 para terminar no 0) e como vai se movimentar(-1).
    print(contador)