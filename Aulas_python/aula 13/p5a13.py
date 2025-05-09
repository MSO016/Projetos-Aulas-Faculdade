# Definição do número secreto
numero_secreto = 7

# Inicialização da variável para guardar o palpite
palpite = 0

# Laço while que continua até acertar
while palpite != numero_secreto:
    # Recebe o palpite do usuário
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
   
    # Verifica se é maior ou menor
    if palpite > numero_secreto:
        print("O número secreto é menor!")
    elif palpite < numero_secreto:
        print("O número secreto é maior!")

# Mensagem quando acerta
print("Parabéns! Você acertou!")