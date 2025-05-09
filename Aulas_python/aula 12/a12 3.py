# Ler os valores de N e M
n = int(input("Digite o valor de M: "))
m = int(input("Digite o valor de N: "))

prod=1
contagempares=0

for i in range(m,n+1):
    if i % 2 ==0:  
        prod *=i
        contagempares +=1 

if contagempares>0:
    print(f"O produtório dos números pares de {m} a {n} é: {prod}")
else:
    print(f"Não há números pares entre {m} e {n}.")