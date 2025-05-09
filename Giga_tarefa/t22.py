salario=float(input("Digite o salário do funcionário: "))
cargo=int(input("Digite o código do cargo (101 - Gerente, 102 - Engenheiro, 103 - Técnico): "))

if cargo == 101:
    percentual=0.10
elif cargo == 102:
    percentual=0.20
elif cargo == 103:
    percentual=0.30
else:
    percentual=0.40

novo_salario=salario * (1 + percentual)
diferenca=novo_salario - salario

print(f"Salário antigo: R${salario:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
print(f"Diferença: R${diferenca:.2f}")
