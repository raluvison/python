import time
import datetime

ano = int(input('Qual ano você quer que eu diga se é bissexto? Ou digite 0 para saber o ano atual:  '))

print('PROCESSANDO...')
time.sleep(2)

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')
