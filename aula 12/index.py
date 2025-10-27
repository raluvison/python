nome = input('Digite seu nome: ')
if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == 'Sofia':
    print(f'Eu te amo {nome}')
elif nome in 'Jett, James, Haiden, Enzo':
    print(f'Você tem um nome de um ótimo piloto de motocross!')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}')