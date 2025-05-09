idade= int(input('Digite sua idade para que avalie se você pode ou não se inscrever: '))

if idade >=18:
   print('Parabéns você pode se inscrever.')
elif 14 <= idade < 16:
   print('Voce pode se inscrever com a assinatura de um adulto.')
else:
   print ('Ainda não possui idade suficiente para a inscrição!')