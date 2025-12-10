import time

exit = False

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while not exit:
    print(
        '   [ 1 ] SOMAR\n'
        '   [ 2 ] MULTIPLICAR\n'
        '   [ 3 ] MAIOR\n'
        '   [ 4 ] NOVOS NÚMEROS\n'
        '   [ 5 ] SAIR'
    )
    choice = int(input('>>>>> Qual é a sua opção? '))
    if choice == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
        print('=-='*10)
        time.sleep(0.5)
    elif choice == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}')
        print('=-='*10)
        time.sleep(0.5)
    elif choice == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
        print('=-='*10)
        time.sleep(0.5)
    elif choice == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif choice == 5:
        print('Finalizando...')
        print('=-='*10)
        print('')
        time.sleep(2)
        exit = True
    else:
        print('Opção inválida! Tente novamente.')
        time.sleep(0.5)
print('Programa finalizado! Volte sempre!')
