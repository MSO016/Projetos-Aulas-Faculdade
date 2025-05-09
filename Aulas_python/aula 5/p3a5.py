print ('este programa pode calcular a distancia percorida por um objeto em queda livre com resistencia do ar')
massa= float(input('massa é: '))
coef_arrasto=float(input('coeficiente é: '))
area_frontal  =float(input('area é: '))
tempo=float(input('o tempo é: '))
densidade_ar=float(input('a densidade é: '))

k = 0.5 * coef_arrasto * area_frontal * densidade_ar
velocidade_terminal = ((2 * massa * 9.81) / (densidade_ar * coef_arrasto * area_frontal)) ** 0.5
fator_exponencial = 2.71828
expoente = (-k * velocidade_terminal * tempo) / massa
termo_exponencial = 1 - fator_exponencial ** expoente
distancia = (massa / k) * velocidade_terminal * termo_exponencial

print ('a distancia percorrida é: '+str (distancia))
