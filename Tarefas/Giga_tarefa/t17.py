altura=float(input("Digite a altura da pessoa em metros: "))
sexo=input("Digite o sexo da pessoa (M para masculino e F para feminino): ").upper()

if sexo == "M":
    peso_ideal=(72.7 * altura) - 58
elif sexo == "F":
    peso_ideal=(62.1 * altura) - 44.7
else:
    peso_ideal=None

if peso_ideal is not None:
    print(f"O peso ideal para a altura {altura}m e sexo {sexo} é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido!")
