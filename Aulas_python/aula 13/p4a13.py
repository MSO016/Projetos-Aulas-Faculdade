# Inicialização das variáveis
soma_total = 0  # Variável para armazenar a soma
numero = 1      # Variável para guardar o número digitado

# Laço while para entrada de números
while numero > 0:  # Condição para continuar enquanto o número for positivo ou zero
    # Solicita entrada do usuário
    numero = float(input("Digite um número (0): "))
   
    # Verifica se o número maior que zero
    if numero > 0:
        soma_total = soma_total + numero

# Mostra o resultado final
print(f"A soma dos números positivos digitados é: {soma_total}")