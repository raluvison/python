
while True:
    try:
        idade = int(input('Digite sua idade: '))
        print(f'Você tem {idade} anos')
        break
    except:
        print('Digite um valor válido!')
        print('')
