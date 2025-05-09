peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
elif imc < 35:
    categoria = "Obesidade grau I"
elif imc < 40:
    categoria = "Obesidade grau II"
else:
    categoria = "Obesidade grau III"

print(f"Seu IMC é {imc:.1f}. Classificação: {categoria}")