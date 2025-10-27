import time

print('-==' * 20)
print('EMPRÉSTIMO BANCÁRIO')
print('-==' * 20)
print('')

print('Digite o valor da casa que deseja: R$', end='')
valor = int(input('\033[32m'))
print('\033[m', end='')
print('Digite seu salário: R$', end='')
salario = int(input('\033[32m'))
print('\033[m', end='')
print('Digite em quantos anos irá pagar: ', end='')
anos = int(input('\033[32m'))
print('\033[m', end='')

parcela = valor / (anos * 12)

print('')
print('PROCESSANDO...')
time.sleep(2)
print('')

if parcela <= salario * 0.3:
    print(f'Financiamento APROVADO!\n' \
    f'Valor do imóvel: R${valor:.2f}\n'
    f'Valor da parcela mínima: R${salario * 0.3:.2f}\n'
    f'Valor da parcela que você ira pagar: R${parcela:.2f}')
else:
    print('Financiamento NEGADO!\n' \
    f'Valor do imóvel: R${valor:.2f}\n'
    f'Valor da parcela mínima: R${salario * 0.3:.2f}\n'
    f'Valor da parcela que você ira pagar: R${parcela:.2f}')