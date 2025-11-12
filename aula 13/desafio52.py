num = int(input('Digite um número: '))

tot = 0
for i in range(1, num+1):
    if num % i == 0:
        print(f'\033[33m {i} \033[m', end='')
        tot += 1
    else:
        print(f'\033[31m {i} \033[m', end='')
    
print(f'\nO número {num} foi divisível {tot} vezes!')

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')
