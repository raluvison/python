import datetime
ano = int(input('Digite seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {(18 - idade) + atual}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {atual - (idade - 18)}.')
else:
    print('VOCÊ DEVE SE ALISTAR IMEDIATAMENTE!')
