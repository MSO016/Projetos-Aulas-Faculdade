hora_inicio=int(input("Digite a hora de início do jogo (0-23): "))
hora_fim=int(input("Digite a hora do final do jogo (0-23): "))

if hora_inicio < 0 or hora_inicio > 23 or hora_fim < 0 or hora_fim > 23:
    print("As horas devem estar entre 0 e 23.")
else:
    if hora_fim >= hora_inicio:
        duracao=hora_fim - hora_inicio
    else:
        duracao=(24 - hora_inicio) + hora_fim

    print(f"Duração do jogo: {duracao} horas")
