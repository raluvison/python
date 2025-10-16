nome = input('Digite o seu nome completo: ')
separado = nome.split()

print(
    f'Nome completo: {nome} \n'
    f'Primeiro nome: {separado[0]} \n'
    f'Ultimo sobrenome: {separado[len(separado) - 1]}'
)