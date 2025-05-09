numeros = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(num)

print("Os números na ordem inversa são:")
for num in reversed(numeros):
    print(num)