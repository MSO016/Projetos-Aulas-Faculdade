nota = float(input("Digite a nota do aluno (0 a 10): "))


if 0 <= nota <= 10:
    
    if nota < 5:
        print("Reprovado")
    elif nota < 6:
        print("Em recuperação")
    else:
        print("Aprovado")
else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")