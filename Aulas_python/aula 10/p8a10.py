# Leia do usuário o valor de N e calcule o produtório de N

# Leia do usuário o valor de P e calcule o produtório de P

# Depois, calcule  resultado = produtorioN/produtorioP

# Mostre resultado

n=int(input("Valor de N: "))
p=int(input("Valor de P: "))

produtorioN = 1
produtorioP = 1

for i in range(1, n+1):
    produtorioN *= i

for i in range(1, p+1):
    produtorioP *= i

resultado = produtorioN/produtorioP

print (f"resultado é: {resultado}")