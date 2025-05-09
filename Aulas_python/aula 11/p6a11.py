# Considere a seguinte maneira de calcular somatória:
# soma=0
# for i in range(1,N):
#      numero = float(input('Informe um valor decimal')
#      soma+= numero

# Leia a quantidade X do usuário e calcule a somatório de X elementos fornecidos pelo usuário

# Leia a quantidade Y do usuário e calcule a somatório de Y elementos fornecidos pelo usuário

# Determine o valor de D, onde:
# D = (SomatoriaX - ProdutorioY)²

x= int(input("Informe um valor: "))
y= int(input("Informe um valor: "))

SomatoriaX=0
ProdutorioY=1

for i in range(1,x+1):
     numero = float(input('Informe um valor decimal: '))
     SomatoriaX+= numero


for i in range(1,y+1):
    numero1 = float(input('Informe um valor decimal: '))
    ProdutorioY*= numero1

d = (SomatoriaX - ProdutorioY)**2

print(f"Este é o resultado do seu N, ou de seus valores: {d}")