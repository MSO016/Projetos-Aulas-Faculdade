idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    
    idades.append(idade)
    alturas.append(altura)

print("\nIdades na ordem inversa:")
for idade in reversed(idades):
    print(idade)

print("\nAlturas na ordem inversa:")
for altura in reversed(alturas):
    print(altura)