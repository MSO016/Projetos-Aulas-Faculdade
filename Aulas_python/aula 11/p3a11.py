# Leia o valor de N do usuário

# Leia N números float do usuário e calcule a somatória destes valores informados pelo usuário.

# Dica:

# soma=0
# for i in range(1,N):
#      numero = float(input('Informe um valor decimal')
#      soma+= numero
n= int(input("Informe um valor: "))
soma=0
for i in range(1,n+1):
     numero = float(input('Informe um valor decimal: '))
     soma+= numero
print(f"Este é o resultado do seu N, ou de seus valores: {soma}")