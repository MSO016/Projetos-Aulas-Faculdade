
total_eleitores=float(input('total: '))
votos_brancos=float(input('brancos: '))
votos_nulos=float(input('nulos: '))
votos_validos=float(input('validos: '))
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100
print(f'percentual brancos: {percentual_brancos}percentual nulos: {percentual_nulos}percentual validos: {percentual_validos}')
