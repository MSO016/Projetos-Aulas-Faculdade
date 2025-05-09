n=int(input("valor n: "))
p=int(input("valor p: "))

somatorio=0
produtorio=1

for i in range(1, n+1):
    somatorio += i

for i in range(1, p+1):
    produtorio *= i

r=somatorio/produtorio

print (f"resultado é: {r}")