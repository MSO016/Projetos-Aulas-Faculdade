# Faça um programa que leia do usuário o seu salário e calcule o imposto: 
# se o salário< 1000 
#    imposto é salario*0.10 
# senão
#    imposto é salario*0.25
s=float(input("Digite o seu salário: "))
if s <1000:
    print(f"O imposto vai ser: {s*0.10}")
else:
    print(f"imposto é salario {s*0.25}")