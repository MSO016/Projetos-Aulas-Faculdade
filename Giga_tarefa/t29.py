numero_identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

media_aproveitamento = (nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7

if media_aproveitamento >= 9.0:
    conceito = "A"
elif media_aproveitamento >= 7.5:
    conceito = "B"
elif media_aproveitamento >= 6.0:
    conceito = "C"
elif media_aproveitamento >= 4.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Número do aluno: {numero_identificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios: {media_exercicios}")
print(f"Média de aproveitamento: {media_aproveitamento:.2f}")
print(f"Conceito: {conceito}")

if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")
