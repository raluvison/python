#Pedra papel e tesoura!
import random

lista = ['pedra', 'papel', 'tesoura']
jogador = input('Escolha pedra, papel ou tesoura: ')
computador = random.choice(lista)

print(f'O jogador escolheu: {jogador}')
print(f'O computador escolheu: {computador}')

if jogador == computador:
    print('Empate, tente novamente!')
elif (jogador == 'pedra' and computador == 'tesoura') or \
        (jogador == 'papel' and computador == 'pedra') or \
            (jogador == 'tesoura' and computador == 'papel'):
    print('O jogador venceu!')
else:
    print('Você perdeu!')
