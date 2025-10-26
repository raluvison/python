from random import randint
import time

computador = randint(0, 5)
print('-==' * 20)
print('Irei pensar em um número de 1 a 5. Tente adivinhar ...')
print('-==' * 20)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)

if jogador == computador:
    print(f'O computador escolheu {computador}\nO jogador escolheu: {jogador}\nVocê venceu!')
else:
    print(f'O computador escolheu {computador}\nO jogador escolheu: {jogador}\nVocê perdeu!')