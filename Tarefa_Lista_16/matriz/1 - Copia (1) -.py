matriz=[]
for i in range(4):
    linha=[]
    for j in range(4):
        valor=int(input(f"digirte o valor para a posição ({i},{j})"))
        linha.append(valor)
    matriz.append(linha)

contagem=sum(1 for linha in matriz for valor in linha if valor >10)

print(f"a matriz possui {contagem} valores maior que 10.")

