n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL'''
)
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual a: {n:b}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a: {n:o}')
elif opção == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a: {n:x}')
else:
    print('Digite uma opção válida!')
