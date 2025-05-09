a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Os valores devem ser inteiros e positivos.")
else:
    if a < b + c and b < a + c and c < a + b:
        semi_perimetro=(a + b + c) / 2
        area=(semi_perimetro * (semi_perimetro - a) * (semi_perimetro - b) * (semi_perimetro - c)) ** 0.5
        print(f"Os valores formam um triângulo.")
        print(f"A área do triângulo é: {area:.2f}")
    else:
        print("Os valores não formam um triângulo.")
        print(f"Valores lidos: a = {a}, b = {b}, c = {c}")
