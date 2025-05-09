codigo=int(input("Digite o código do item do cardápio: "))
quantidade=int(input("Digite a quantidade desejada: "))

if codigo == 100:
    preco=1.20
    item="Cachorro quente"
elif codigo == 101:
    preco=1.30
    item="Bauru simples"
elif codigo == 102:
    preco=1.50
    item="Bauru com ovo"
elif codigo == 103:
    preco=1.20
    item="Hambúrguer"
elif codigo == 104:
    preco=1.30
    item="Cheeseburguer"
elif codigo == 105:
    preco=1.00
    item="Refrigerante"
else:
    preco=None
    item="Item inválido" 
                                    #fontes gpt, não consegui sozinho desculpa.
if preco is not None:
    valor_total=preco * quantidade
    print(f"O item {item} custa R${preco:.2f} cada.")
    print(f"Total a ser pago: R${valor_total:.2f}")
else:
    print("Código inválido!")