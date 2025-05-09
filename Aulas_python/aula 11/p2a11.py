n=int(input("Digite o valor de N: "))
k=int(input("Digite o valor de K: "))
somatorioN= 0
somatorioK= 0

for i in range(1, n+1):
    somatorioN += i


for i in range(1, k+1):
    somatorioK += i

resultado= somatorioK - (somatorioN**2)
print(f"O resultado é: {resultado:.2f}")

