numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

print("Os números digitados são:")
for num in numeros:
    print(num)