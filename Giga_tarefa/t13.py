numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
numero3=int(input("Digite o terceiro número: "))

maior=numero1

if numero2 > maior:
    maior=numero2
if numero3 > maior:
    maior=numero3

print(f"O maior número é:{maior}")
