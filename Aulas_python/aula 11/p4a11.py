n= int(input("Informe um valor: "))
produtorio=1
for i in range(1,n+1):
     numero = float(input('Informe um valor decimal: '))
     produtorio*= numero
print(f"Este é o resultado do seu N, ou de seus valores: {produtorio}")