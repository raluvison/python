n1 = input('Digite algo: ')

print (
    f'Seu tipo primitivo é: {type(n1)} \n'
    f'Ele é alphanumérico?? {n1.isalnum()} \n'
    f'Ele é um alpha? {n1.isalpha()} \n'
    f'Ele é ? {n1.isascii()} \n'
    f'Ele é decimal? {n1.isdecimal()} \n'
    f'Ele é um digito? {n1.isdigit()} \n'
    f'Ele é {n1.isidentifier()} \n'
    f'Ele está todo em minúsculo? {n1.islower()} \n'
    f'Ele é numérico? {n1.isnumeric()} \n'
    f'Ele {n1.isprintable()} \n'
    f'Ele {n1.isspace()} \n'
    f'Ele está todo em maiúsculo? {n1.isupper()} \n'
    f'Ele é um título? {n1.istitle()}'
)