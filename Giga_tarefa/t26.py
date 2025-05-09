valor=float(input("Digite um valor em reais: "))
notas100=int(valor // 100)
valor %= 100
notas50=int(valor // 50)
valor %= 50
notas10=int(valor // 10)
valor %= 10
notas5=int(valor // 5)
valor %= 5
notas1=int(valor)

print(f"Valor lido: {valor:.2f} reais")
print(f"Notas de 100: {notas100}")
print(f"Notas de 50: {notas50}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 5: {notas5}")
print(f"Notas de 1: {notas1}")
