#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, o nome com todas minúsculas, quantas letras ao todo(sem contar espaços) e quantas letras tem o primeiro nome.
nome = input('Digite o seu nome completo: ')
print(f'Seu nome todo em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome todo em letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras!')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras!')

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras!')