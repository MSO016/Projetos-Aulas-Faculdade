print("=== Usando FOR ===")
# No FOR, o range já controla o início, fim e incremento
for numero in range(1, 6):  # O range vai de 1 até 5 
    print(f"Contagem: {numero}")


print("\n=== Usando WHILE ===")
# No WHILE, precisamos controlar tudo manualmente
contador = 1           # Precisamos inicializar o contador
while contador <= 5:   # Precisamos definir quando parar
    print(f"Contagem: {contador}")
    contador = contador + 1  # Precisamos incrementar manualmente