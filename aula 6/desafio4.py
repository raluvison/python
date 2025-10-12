n1 = input('Digite algo: ')

print (
    f'Seu tipo primitivo é: {type(n1)} \n'
    f'Ele é alfanumérico?? {n1.isalnum()} \n'
    f'Ele é um alfabético? {n1.isalpha()} \n'
    f'Ele está todo em minúsculo? {n1.islower()} \n'
    f'Ele é numérico? {n1.isnumeric()} \n'
    f'Ele só tem espaços? {n1.isspace()} \n'
    f'Ele está todo em maiúsculo? {n1.isupper()} \n'
    f'Ele está capitalizado? {n1.istitle()}'
)