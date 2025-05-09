import math

n1=float(input("N 1: "))
n2=float(input("N 2: "))

if n1>n2:
    resultado= math.pow(n1,n2)
    print(f"se n1 for maior que n2, o resultado sera: {resultado}")
elif n1<n2:
    resultado= math.pow(n2,n1)
    print(f"se n2 for maior que n1, o resultado será: {resultado}")
else:
    resultado= math.pow(n1,n2)
    print(f"se os numero forem iguais o reusultado será: {resultado}")