#atribuindo tamanho ao vetor
vetor1 = [0] * 5
for i in range(5):
    vetor1[i] = int(input(f"Digite o {i+1}º número: "))

############################################################

vetor2 = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor2.append(numero)

for i in range(5):
   print (vetor1[i])

for i in range(5):
   print (vetor2[i])


#a diferença é que um vc precisa atribuir o limite, e o outro não.