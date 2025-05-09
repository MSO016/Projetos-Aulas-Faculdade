tamanho=int(input("oi digite o tamnho do vetor: "))

vetor=[]

for i in range(tamanho):
    elementos=int(input(f"informe os elemntos do vetor: {i + 1}: "))
    vetor.append(elementos)

print("Elementos negativos do vetor: ")
for num in vetor:
    if num < 0:
        print(num)