codigo=int(input("Digite o código do produto: "))
quantidade=int(input("Digite a quantidade comprada: "))

if codigo == 1001:
    preco_unitario=5.32
elif codigo == 1324:
    preco_unitario=6.45
elif codigo == 6548:
    preco_unitario=2.37
elif codigo == 987:
    preco_unitario=5.32
elif codigo == 7623:
    preco_unitario=6.45
else:
    preco_unitario=None

if preco_unitario is not None:
    preco_total=preco_unitario * quantidade
    print(f"Preço total devido: R${preco_total:.2f}")
else:
    print("Código do produto inválido!")
