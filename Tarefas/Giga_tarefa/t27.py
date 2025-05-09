ipi=float(input("Digite a percentagem do IPI: "))
codigo1=int(input("Digite o código da peça 1: "))
valor_unitario1=float(input("Digite o valor unitário da peça 1: "))
quantidade1=int(input("Digite a quantidade da peça 1: "))

codigo2=int(input("Digite o código da peça 2: "))
valor_unitario2=float(input("Digite o valor unitário da peça 2: "))
quantidade2=int(input("Digite a quantidade da peça 2: "))

valor_total=(valor_unitario1 * quantidade1 + valor_unitario2 * quantidade2) * (ipi / 100 + 1)

print(f"Valor total a ser pago: R$ {valor_total:.2f}")
