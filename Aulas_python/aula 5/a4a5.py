populacao_inicial=int(input('digite a população inicial: '))
taxa_crescimento=float(input('digite a taxa de crescimento mas em porcentagem: '))
anos=int(input('digita quantos anos: '))
população_futura =int(populacao_inicial*(1 + taxa_crescimento))**anos
print ('resultado: '+str(população_futura))