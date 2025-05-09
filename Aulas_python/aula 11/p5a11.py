# Leia o valor de K, L, N e M
# calcule o somatório de K
# calcule o produtório de L
# calcule a somatória de N
# calcule o produtório de M

# Determine o índice I, onde:
# IC = (SomatorioK * ProdutorioL) / (SomatorioN + ProdutorioM)

k= int(input("Informe um valor de K: "))
l= int(input("Informe um valor de L: "))
n= int(input("Informe um valor de N: "))
m= int(input("Informe um valor de M: "))

somatoriok=0
somatorion=0
produtoriol=1
produtoriom=1

for i in range(1, k+1):
    somatoriok += i

for i in range(1, n+1):
    somatorion += i

for i in range(1, l+1):
    produtoriol *= i

for i in range(1, m+1):
    produtoriom *= i

ic = (somatoriok * produtoriol) / (somatorion + produtoriom)

print(f"Este é o resultado do seus valores: {ic:.2f}")