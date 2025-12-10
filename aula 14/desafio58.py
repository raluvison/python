from random import randint

print(
    'Sou seu computador...\n'
    'Acabei de pensar em um número entre 0 a 10.\n'
    'Será que você consegue adivinhar qual foi?'
)
comp = randint(0, 10) #escolha do computador
cont = 0 #contador de palpites
correct = False #correto é falso pois ainda o jogador não acertou
while not correct: #enquanto não estiver correto
    r = int(input('Qual seu palpite? '))
    cont += 1 #Ele vai ler um número e adicionar 1 ao contador
    if r == comp:
        correct = True #se o jogador for igual ao computador, correto passa a ser True e quebra o loop
    else:
        if r < comp:
            print('Mais... Tente novamente!')
        elif r > comp:
            print('Menos... Tente novamente!')
print(f'Você acertou em {cont} tentativas!')