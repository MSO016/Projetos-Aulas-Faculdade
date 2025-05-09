# Faça um algoritmo que leia as 3 ns de um aluno e calcule a média final deste aluno. Considerar
#  que a média é ponderada e que o p das ns é: 2,3 e 5, respectivamente.

n1 = float(input("Digite a primeira nota (peso 2): "))
n2 = float(input("Digite a segunda nota (peso 3): "))
n3 = float(input("Digite a terceira nota (peso 5): "))

p1 = 2
p2 = 3
p3 = 5

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f"A média final do aluno é: {media:.2f}")