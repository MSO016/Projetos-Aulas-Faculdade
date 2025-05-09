#dt=dias totais; dr=dias restantes; a=anos; m=mes;

dt = int(input("Digite sua idade em dias: "))

a = dt//365
dr = dt%365 

m = dr//30
d = dr%30 

print(f"Sua idade é: {a} anos, {m} meses e {d} dias.")