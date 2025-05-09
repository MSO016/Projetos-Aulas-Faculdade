tamanho= int(input("digite o tamanho do vetor: "))

vetor=[]

for i in range(tamanho):
    elemento=int(input(f"digite o elemento {i+1}: "))
    vetor.append(elemento)

numero=int(input("Digite um numero para a multiplicar os elemntos do vetor: "))

for i in range(tamanho):
    vetor[i]*=numero

print("vetor apos a multiplicação: ")

print(vetor)
