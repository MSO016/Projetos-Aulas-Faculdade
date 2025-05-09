#Pergunte o valor de N para o usuário e depois leia N 
# valores decimais do usuário calculando a seguinte somatória
#SN += (valor_decimal* (valor_decimal+ 1)) / 2
#Pergunte o valor de P para o usuário e depois leia P valores 
# decimais do usuário calculando o seguinte produtorio
#PP *= (valor_decimal + (SN * 0.1)) / P
#Finalmente calcule:
#resultado = (SN/PP)^0.5

n = int(input("Digite o valor de N: "))
p = int(input("Digite o valor de P: "))

sn = 0
pp = 1

for i in range(1, n+1):
    vd= float(input('Informe um valor decimal (vd): '))
    sn += (vd * (vd + 1)) / 2

for i in range(1, p+1):
    pp *= (vd + (sn * 0.1)) / p

r = (sn/pp)**0.5

print(f"Este é o resultado, de seus valores: {r:.2f}")