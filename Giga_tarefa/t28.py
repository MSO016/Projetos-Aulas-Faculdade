hora_inicio=int(input("Digite a hora de início do jogo: "))
minuto_inicio=int(input("Digite o minuto de início do jogo: "))
hora_fim=int(input("Digite a hora de término do jogo: "))
minuto_fim=int(input("Digite o minuto de término do jogo: "))

if minuto_fim < minuto_inicio:
    minuto_fim += 60
    hora_fim -= 1

duracao_horas=hora_fim - hora_inicio
duracao_minutos=minuto_fim - minuto_inicio

if duracao_horas < 0:
    duracao_horas += 24

print(f"Duração do jogo: {duracao_horas} horas e {duracao_minutos} minutos")
