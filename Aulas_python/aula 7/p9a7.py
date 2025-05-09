# Leia os valores de X e Y

# Se X >= Y calcule a raiz de X-Y
# Senão, calcula a raiz de Y-X
import math
x=float(input("digite o valor de x: "))
y=float(input("digite o valor de y: "))

if x>=y:
    resultado= math.sqrt (x-y)
    print(f"A raiz quadrada de x - y é: {resultado:.2f}")
else:
    resultado = math.sqrt(y - x)
    print(f"A raiz quadrada de Y - X é: {resultado:.2f}")