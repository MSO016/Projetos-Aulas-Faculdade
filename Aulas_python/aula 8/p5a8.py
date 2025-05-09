# Observe o programa a seguir e adapte-o para o seguinte problema:
# Leia o salario do usuário.
# Se o salario for menor que 2500 o imposto é de 380 reais
# Se o salario for maior que 2500 o imposto é de 430 reais
# senão, o imposto é de 405 reais

numero = float(input("Digite um salario: "))
# salario= 2500-380
if numero < 2500:
    salario= 2500-380
    print(f"O número é: {salario:.2f}")
elif numero > 2500:
    salario= 2500-430
    print(f"O número é: {salario:.2f}")
else:
    imposto=2500-405
    print(f"O número é: {imposto:.2f}")