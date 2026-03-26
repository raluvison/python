print('GERADOR DE PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1

while cont <= 10:
    print(f'{n1} -> ', end='')
    n1 += r
    cont += 1 
print('FIM')