frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
contrario = junto[::-1]

print(f'O contrário de {junto} é {contrario}!')
if contrario == junto:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')