from io import RawIOBase


print ('Este programa que calcule a força centrípeta necessária para manter um objeto em movimento circular uniforme')
massa= float(input('Digite a massa para este calculo: '))
velocidade_tangencial=float(input('Digite a velocidade tangencial para este calculo: '))
raio=float(input('Digite o raio para este calculo: '))
força_centrípeta = (massa * velocidade_tangencial ** 2) / raio
print (f'a força centripeta é: {força_centrípeta}')