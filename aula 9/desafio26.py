frase = input('Digite alguma frase: ').strip().upper()

print(
    f'Quantas vezes apareceu o A: {frase.count('A')} \n'
    f'Em qual posição ela apareceu a primeira vez: {frase.find('A')+1} \n'
    f'Em qual posição ela apareceu a última vez: {frase.rfind('A')+1}'
)