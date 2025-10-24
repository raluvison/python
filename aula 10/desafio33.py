n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o MAIOR número')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o MAIOR número')
else:
    print(f'{n3} é o MAIOR número')

if n1 < n2 and n1 < n3:
    print(f'{n1} é o MENOR número')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o MENOR número')
else:
    print(f'{n3} é o MENOR número')