# Crie um programa que:
# leia o tamanho do vetor do usuário
# leia os elementos do vetor1 do usuário
# leia os elementos do vetor2 do usuário
# gere um novo vetor3 com a soma dos elementos do vetor1 e vetor2
# DICA:
# vetor3[] = [0] * tamanho
# for i in range(tamanho):
#     vetor3[i] = vetor1[i] + vetor2[i]

tamanho= int(input("digite o tamanho do vetor: "))

v1=[]
print("digite os elementos do vetor 1: ")
for i in range(tamanho):
    elemento=int(input(f"digite o elemento {i+1} do vetor 1: "))
    v1.append(elemento)
v2=[]
print("digite os elementos do vetor 2: ")
for i in range(tamanho):
    elemento=int(input(f"digite o elemento {i+1} do vetor 2: "))
    v2.append(elemento)

v3=[0]*tamanho
for i in range(tamanho):
    v3[i] = v1[i] + v2[i]

print("Vetor3 (soma de vetor1 e vetor2): ")
print(v3)