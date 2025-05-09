# Faça um programa que leia a idade do usuário.
idade=float(input("Digite sua idade: "))
if idade < 18: 
    print("menor de idade")
elif idade < 60:  
    print("adulto")
else: 
    print("idoso")