def triangulo_de_pascal(n):
    triangulo = [[1]]
    for i in range(1, n):
        linha_anterior = triangulo[-1]
        nova_linha = [1]
        for j in range(1, i):
            nova_linha.append(linha_anterior[j-1] + linha_anterior[j])
        nova_linha.append(1)
        triangulo.append(nova_linha)
    return triangulo

n = int(input("Digite um número inteiro positivo: "))

triangulo = triangulo_de_pascal(n)

print("Triângulo de Pascal:")
for linha in triangulo:
    print(" ".join(map(str, linha)))
