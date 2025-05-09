# leia os valores de A, B e C

# se C for diferente de zero:
# if C != 0:
#    X =  (A+B)/C
# else:
#    print ('não existe valor de X')
A=float(input("Digite o valor de A: "))
B=float(input("Digite o valor de B: "))
C=float(input("Digite o valor de C: "))

if C!= 0:
    X=(A+B)/C
    print(f"O valor de X é: {X}")
else:
    print("Não existe valor de X")