nota= int(input('Digite sua nota para que avalie se foi aprovado ou não: '))

if nota >=7:
    print('Você passou parabéns!!!')
elif 4 <= nota < 7:
    print('Você ficara de recuperação, portanto ATENÇÃO!!!')
else:
    print('Você não passou mas não desista!!!')