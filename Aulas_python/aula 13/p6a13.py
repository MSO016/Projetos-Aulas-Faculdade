from random import randint

# Sorteia um número do DADO entre 1 e 6
dado = randint(1, 6)

# Inicializa as variáveis
tentativas = 0
numero=0

# Loop principal do jogo
while numero != dado:
    numero = int(input("Digite um número entre 1 e 6: "))
    tentativas = tentativas + 1
   
    if numero == dado:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")