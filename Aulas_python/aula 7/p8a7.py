# Faça um programa que leia do usuário um valor float.
# Se o valor for maior que zero, mostrar a raiz quadrada do número, senão, mostrar "não existe raiz de número negativo"
import math
u=float(input("digite um numero para uma raiz: "))
if u>0:
    print(f"a raiz quadrada é: {math.sqrt (u)} ")
else:
    print("não existe raiz de número negativo")
    