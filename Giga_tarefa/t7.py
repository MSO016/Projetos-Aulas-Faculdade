custofabrica=float(input("Digite o custo de fábrica do carro: "))

percentualdistribuidor=0.28
percentualimpostos=0.45

custodistribuidor=custofabrica*percentualdistribuidor
custoimpostos=custofabrica*percentualimpostos
custoconsumidor=custofabrica+custodistribuidor+custoimpostos

print(f"O custo ao consumidor é: {custoconsumidor}")