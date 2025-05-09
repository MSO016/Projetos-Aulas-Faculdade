# Teste o seguinte programa

# import random
# # Sorteio do número do dado
# dado = random.randint(1, 6)
# print(f"O número sorteado foi {dado}.")

# Agora altere o programa para que seja lido do usuário um número e que verifique se o usuário acertou o número do dado
import random
dado = random.randint(1, 6)
print(f"O número sorteado foi {dado}.")

numero_usuario = int(input("Adivinhe o número do dado (de 1 a 6): "))

if numero_usuario == dado:
    print("Parabéns! Você acertou o número do dado.")
else:
    print("Que pena! Você errou. Tente novamente.")