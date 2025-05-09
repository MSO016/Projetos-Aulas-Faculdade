
tamanho=int(input("digite o tamnho do vetor"))

vetor=[]

for i in range(tamanho):
    elemento= float(input(f"digite o elemnto {i+1}: "))
    vetor.append(elemento)

n=float(input("Digite o valor de n diferente de zero: "))
if n==0:
    print("o valor de n não pode ser zero.")
else:
    vr=[elemento / n for elemento in vetor]
    
print("Resultado após a divisão dos elementos por n: ")
print(vr)#vr=vetor resultado