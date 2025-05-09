numero=int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    par_impar="par"
else:
    par_impar="ímpar"

if numero >= 0:
    sinal="positivo"
else:
    sinal="negativo"

print(f"O número {numero} é {par_impar} e {sinal}.")
