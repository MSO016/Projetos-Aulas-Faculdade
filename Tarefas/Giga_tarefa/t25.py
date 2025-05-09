i=int(input("Digite um valor inteiro positivo (1, 2 ou 3): "))
a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))

print(f"Valores lidos: a = {a}, b = {b}, c = {c}")

if i == 1:
    valores=sorted([a, b, c])
    print(f"Valores em ordem crescente: {valores}")
elif i == 2:
    valores=sorted([a, b, c], reverse=True)
    print(f"Valores em ordem decrescente: {valores}")
elif i == 3:
    maior=max(a, b, c)
    valores=[x for x in (a, b, c) if x != maior]
    print(f"Valores com o maior no meio: {valores[0]}, {maior}, {valores[1]}")
else:
    print("Valor de i inválido!")
