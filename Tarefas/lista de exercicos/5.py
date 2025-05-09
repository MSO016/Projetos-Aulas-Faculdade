numeros = []
par = []
impar = []

for i in range(20):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
    
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("Vetor de números:", numeros)
print("Vetor de números pares:", par)
print("Vetor de números ímpares:", impar)