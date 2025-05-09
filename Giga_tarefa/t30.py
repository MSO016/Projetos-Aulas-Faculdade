indice_poluicao = float(input("Digite o índice de poluição medido: "))

if indice_poluicao > 0.25 and indice_poluicao < 0.3:
    print("Índice aceitável.")
elif indice_poluicao >= 0.3 and indice_poluicao < 0.4:
    print("Indústrias do 1º grupo devem suspender suas atividades.")
elif indice_poluicao >= 0.4 and indice_poluicao < 0.5:
    print("Indústrias do 1º e 2º grupo devem suspender suas atividades.")
elif indice_poluicao >= 0.5:
    print("Todas as indústrias dos 3 grupos devem paralisar suas atividades.")
else:
    print("Índice de poluição dentro dos limites aceitáveis.")
