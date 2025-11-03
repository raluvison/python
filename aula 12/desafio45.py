import random
import time

print(
    'Suas opções:\n'
    '[ 1 ] PEDRA\n'
    '[ 2 ] PAPEL\n'
    '[ 3 ] TESSOURA'
)

while True:
    jogador = int(input('Qual é a sua jogada? '))
    if jogador == 1:
        jogador = 'PEDRA'
        break
    elif jogador == 2:
        jogador = 'PAPEL'
        break
    elif jogador == 3:
        jogador = 'TESOURA'
        break
    else:
        print('Escolha uma opção válida!')
        print('')
opções = ['PEDRA' , 'PAPEL', 'TESOURA']
computador = random.choice(opções)

print('')
print('PEDRA...')
time.sleep(1)
print('PAPEL ou')
time.sleep(1)
print('TESOURA!')
time.sleep(0.5)
print('-==' * 20)
print(
    f'O JOGADOR escolheu {jogador}\n'
    f'O COMPUTADOR escolheu {computador}')
print('-==' * 20)
