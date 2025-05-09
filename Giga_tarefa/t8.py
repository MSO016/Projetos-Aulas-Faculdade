a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
d=float(input("Digite o valor de d: "))
e=float(input("Digite o valor de e: "))
f=float(input("Digite o valor de f: "))

denominador=(a*e-b*d)
x=(c*e-b*f)/denominador
y=(a*f-c*d)/denominador

print(f"O valor de x é:{x}")
print(f"O valor de y é:{y}")
