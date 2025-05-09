# Crie um programa que:
# leia do usuário o tamanho do vetor
# leia do usuário dos elementos do vetor
# leia do usuário um outro valor X
# com um FOR conte quantas vezes o elemento X aparece no vetor
# mostre o resultado
# dica:
# contador=0
# for i in range(tamanho):
#      if vetor[i] = X:
#           contador++;

tamanho= int(input("Digite o tamnho do seu vetor: "))

vetor=[]
print("digite os elementos do vetor: ")
for i in range(tamanho):
    elemento=int(input(f"Digite o elemento do vetor {i+1}: "))
    vetor.append(elemento)

x=int(input("digite o valor x para procurar no vetor: "))

contador=0
for i in range(tamanho):
    if vetor[i] == x:
        contador+=1

print(f"o valor {x} aparece {contador} vezes no vetor.")