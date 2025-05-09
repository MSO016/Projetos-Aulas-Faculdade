#Leia o valor de N do usuário
#Leia N números decimais do usuário 
#
#Depois calcule a somatória dos valores que são divisores do próprio N
#soma_divisores=0
#for i in range(1, N):
#  if N % i == 0:
#    soma_divisores += i

#Um número perfeito é aquelas cuja soma dos seus divisores próprios (excluindo ele mesmo) é igual ao próprio número.
#Então, use o IF e verifique se N é um número perfeito

n=int(input("Digite um número inteiro N: "))

sd=0

for i in range(1,n):
    if n % i == 0:
        sd += i

if sd == n:
   print(f"{n} é um número perfeito.")
else:
   print(f"{n} não é um número perfeito.")