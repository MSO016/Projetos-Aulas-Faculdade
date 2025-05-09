#Crie um programa que:
#leia do usuário o vetorA de 10 posições.
#leia do usuário o vetorB de 10 posições.
#calcula o vetorC[i] = vetorA[i] + vetorB[i]
#mostrar o resultado

vetora= []
vetorb= []
vetorc= [] 

for i in range(10):
    numeroa = int(input(f"Digite o {i+1}º número A: "))
    vetora.append(numeroa)
   

for i in range(10):
    numerob = int(input(f"Digite o {i+1}º número B: "))
    vetorb.append(numerob)

for i in range(10):
    numeroc = vetora[i]+vetorb[i]
    vetorc.append(numeroc)
    print(f"o resultado do vetor C: {vetorc[i]}")





