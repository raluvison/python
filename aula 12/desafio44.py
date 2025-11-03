print('='*20, 'LOJAS LUVISON', '='*20)
valor = float(input('Preço das compras: '))

print(
    'FORMAS DE PAGAMENTO\n'
    '[ 1 ] à vista dinheiro/pix\n'
    '[ 2 ] à vista cartão\n'
    '[ 3 ] 2x no cartão\n'
    '[ 4 ] 3x no cartão'
)
    
while True:
    opção = int(input('Selecione a opção: '))
    desconto10 = valor * 0.1
    desconto5 = valor * 0.5
    juros20 = valor * 0.2

    if opção == 1:
        total = valor - desconto10
        break
    elif opção == 2:
        total = valor - desconto5
        break
    elif opção == 3:
        total = valor
        parcela = valor / 2
        print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!')
        break
    elif opção == 4:
        parcelas = int(input('Quantas parcelas vão ser? '))
        total = (valor + juros20) / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${total:.2f} COM JUROS!')
        break
    else:
        print('Escolha uma opção válida!')
        print('')
print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')