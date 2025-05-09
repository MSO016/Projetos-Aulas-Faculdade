segundostotais=int(input("Digite o tempo de duração do evento em segundos: "))

horas=segundostotais//3600
segundosrestantes=segundostotais%3600
minutos=segundosrestantes//60
segundos=segundosrestantes%60

print(f"O tempo de duração é: {horas} horas, {minutos} minutos e {segundos} segundos.")