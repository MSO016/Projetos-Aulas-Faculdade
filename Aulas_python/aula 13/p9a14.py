n = int(input("Digite um número até o qual deseja ver os números pares: "))


print("Números pares usando FOR:")
for i in range(2, n + 1, 2):
    print(i)

print("\nNúmeros pares usando WHILE:")
i = 2
while i <= n:
    print(i)
    i += 2