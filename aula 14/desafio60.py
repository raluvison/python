n = int(input('Digite um número para calcular seu fatorial: '))

original_n = n
fatorial = 1
cont = n

print(f'Calculando {original_n}!', end=' ')

while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' ', end='')
    cont -= 1

while n > 1:
    fatorial *= n
    n -= 1

print(f'= {fatorial}')