valores = []
for i in range(10):
    valor = float(input(f"Digite o valor para a posição {i}: "))
    valores.append(valor)

valores_iguais = set([x for x in valores if valores.count(x) > 1])

if valores_iguais:
    print("Valores iguais encontrados:", valores_iguais)
else:
    print("Não há valores iguais no vetor.")
