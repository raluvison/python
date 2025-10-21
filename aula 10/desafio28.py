import random

print('Irei pensar em um número de 1 a 5...')
jogador = int(input('Tente adivinhar qual número irei escolher: '))
numeros = range(1, 6)
computador = random.choice(numeros)
if jogador == computador:
    print(f'O COMPUTADOR escolheu: {computador}. O JOGADOR escolheu: {jogador}. \nVocê venceu!')
else:
    print(f'O COMPUTADOR escolheu: {computador}. O JOGADOR escolheu: {jogador}. \nVocê perdeu!')