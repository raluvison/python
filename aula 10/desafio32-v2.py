ano = int(input('Digite um ano e eu direi se ele é bissexto: '))
if ano % 400 == 0:
    print('Ele é bissexto!')
elif ano % 100 == 0:
    print('Ele não é bissexto!')
elif ano % 4 == 0:
    print('Ele é bissexto!')
else:
    print('Ele não é bissexto!')