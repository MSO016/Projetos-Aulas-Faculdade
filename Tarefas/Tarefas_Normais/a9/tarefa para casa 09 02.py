# valor_compra = float(input("Digite o valor da compra: "))

# if valor_compra < 100:
#     desconto = 0
#     valor_final = valor_compra
# elif 100 <= valor_compra <= 500:
#     desconto = valor_compra * 0.10  
#     valor_final = valor_compra - desconto
# else:
#     desconto = valor_compra * 0.15  
#     valor_final = valor_compra - desconto

# print(f"Valor da compra: R$ {valor_compra:.2f}")
# print(f"Desconto aplicado: R$ {desconto:.2f}")
# print(f"Valor final a pagar: R$ {valor_final:.2f}")

valorc=float(input("Digite o valor da compra: "))

if valorc<100:
    desconto= 0
    valorf=valorc
elif 100<=valorc <=500:
    desconto= valorc*0.10
    valorf=valorc-desconto
else:
    desconto=valorc*0.15
    valorf=valorc-desconto
