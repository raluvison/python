while True:
    try:
        numero = int(input('Digite um número: '))
        print(10 / numero)
        break
    except ValueError:
        print('Digite um número válido!')
        print('')
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
        print('')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        print('')