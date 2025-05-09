# Ler os valores do vetor x
x = []
print("Digite os valores para o vetor x:")
for i in range(5):
    valor = int(input(f"Posição {i}: "))
    x.append(valor)

y = []
print("Digite os valores para o vetor y:")
for i in range(5):
    valor = int(input(f"Posição {i}: "))
    y.append(valor)

soma = [x[i] + y[i] for i in range(5)]

produto = [x[i] * y[i] for i in range(5)]

diferenca = [valor for valor in x if valor not in y]

intersecao = list(set(x) & set(y))

uniao = list(set(x) | set(y))

print("Soma entre x e y:", soma)
print("Produto entre x e y:", produto)
print("Diferença entre x e y:", diferenca)
print("Interseção entre x e y:", intersecao)
print("União entre x e y:", uniao)
