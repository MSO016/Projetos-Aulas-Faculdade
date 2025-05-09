codigo=int(input("Digite o código do aluno: "))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))

maior=max(nota1, nota2, nota3)

if maior==nota1:
    media=(nota1*4 + nota2*3 + nota3*3) / 10
elif maior==nota2:
    media=(nota2*4 + nota1*3 + nota3*3) / 10
else:
    media=(nota3*4 + nota1*3 + nota2*3) / 10

status="APROVADO" if media >= 5 else "REPROVADO"

print(f"Código do aluno:{codigo}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média ponderada:{media:.2f}")
print(status)
