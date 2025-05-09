nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
opcao=int(input("Escolha o tipo de média (1 - Aritmética, 2 - Ponderada, 3 - Harmônica): "))

if opcao == 1:
    media=(nota1 + nota2 + nota3) / 3
elif opcao == 2:
    media=(nota1*3 + nota2*3 + nota3*4) / (3 + 3 + 4)
elif opcao == 3:
    media=3 / ((1 / nota1) + (1 / nota2) + (1 / nota3))
else:
    media=None

if media is not None:
    print(f"A média calculada é: {media:.2f}")
else:
    print("Opção inválida!")
