print ("Este programa lhe apresentara quanto o usuário ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês")
ganhoh=float(input('Digite o valor do seu ganho por hora: '))
horast=float(input('Digite o valor das horas trabalhadas por mês: '))
salario=ganhoh*horast
ir= salario*0.11
inss=salario*0.08
sindicato=salario*0.05
liquido= salario-ir-inss-sindicato
print(f'''
  Salario bruto é: {salario}
  Salrio Liquido é: {liquido}
  Desconto do Imposto de renda é: {ir}
  Desconto do INSS é: {inss}
  Desconto Sindical é: {sindicato}
  ''')