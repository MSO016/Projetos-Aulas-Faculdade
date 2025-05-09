import math

x1= float(input("Leia as coordenadas do primeiro ponto: "))
y1= float(input("Leia as coordenadas do primeiro ponto: "))
z1= float(input("Leia as coordenadas do primeiro ponto: "))

x2= float(input("Leia as coordenadas do segundo ponto: "))
y2= float(input("Leia as coordenadas do segundo ponto: "))
z2= float(input("Leia as coordenadas do segundo ponto: "))

n=(x2-x1)**2+(y2-y1)**2+(z2-z1)**2
raiz= math.sqrt(n)
print(f'mostre a distancia: {raiz:.2f}')    
