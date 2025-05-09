import math

angulo = float(input("Digite um ângulo em graus: "))
seno = math.sin(math.radians(angulo))

print(f"O seno de {angulo} graus é {seno:.4f}")

d = math.sqrt(angulo*seno)

print (f'O valor do angulo em graus é: {d:.2f}')