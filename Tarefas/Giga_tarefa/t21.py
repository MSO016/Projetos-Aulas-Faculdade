codigo=input("Digite o código do produto: ")
quantidade=int(input("Digite a quantidade comprada: "))

if codigo == 'ABCD':
    preco_unitario=5.30
elif codigo == 'XYPK':
    preco_unitario=6.00
elif codigo == 'KLMP':
    preco_unitario=3.20
elif codigo == 'QRST':
    preco_unitario=2.50
else:
    preco_unitario=None

if preco_unitario is not None:
    preco_total=preco_unitario * quantidade
    print(f"Preço total devido: R${preco_total:.2f}")
else:
    print("Código do produto inválido!")
