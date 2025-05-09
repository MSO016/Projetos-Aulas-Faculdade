print ("calcule a potencia do aparelho em watts: ")
w= int(input("Número de watts: "))
h= int(input("Número de horas de uso por dia: "))
c= int(input("Custo do kWh: "))
consumo_diario= (w*h) / 1000 
custo_diario= consumo_diario * c
print ("consumo diario é: "+str(consumo_diario)+" custo diario é: "+str(custo_diario))