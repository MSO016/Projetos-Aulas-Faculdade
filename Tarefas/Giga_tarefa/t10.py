a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))

maiorab=(a+b+abs(a-b))/2
maiortres=(maiorab+c+abs(maiorab-c))/2

print(f"Os valores lidos são: a={a}, b={b}, c={c}")
print(f"{maiortres} é o maior")
