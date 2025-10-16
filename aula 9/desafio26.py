frase = input('Digite alguma frase: ')

print(
    f'Quantas vezes apareceu o a: {frase.count('a')} \n'
    f'Em qual posição ela apareceu a primeira vez: {frase.find('a')} \n'
    f'Em qual posição ela apareceu a última vez: {frase.rfind('a')}'
)