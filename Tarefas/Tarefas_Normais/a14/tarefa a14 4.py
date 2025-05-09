print("For")

numero=int(input("Digite um número: "))
soma=0

contador=1

while contador <=numero:
    soma +=contador
    contador +=1

print(f"A somatória de 1 até {numero} é {soma}")


print ("While")


numero1=int(input("Digite um número: "))
soma1=0

for i in range(1,numero1+1):
    soma1+=i

print(f"A somatória de 1 até {numero1} é {soma1}.")

#########################################################################################################################################################

# While é feito de forma manual tendo que usar o soma +contador + 1
# Enquanto o For segue as sequencias de forma automaticas sendo mais pratico.

#########################################################################################################################################################