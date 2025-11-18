# Definindo inicio da cor e final para utilizar nas respostas
corverde_inicio = '\033[32m'
corverde_final = '\033[m'
soma = 0 # Soma para descobrirmos o total dos valores das idades e depois dividir por 4 para encontrar a média
total_mulher_20 = 0 #Acumulador para o total de mulheres abaixo de 20 anos
maior_idade = -1 # Garante que qualquer homem digitado terá idade maior que esse número
maior_idade_nome = '' # Acumulador para registrar o nome do mais velho

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    
    nome = str(input(f'Nome: {corverde_inicio}')).title().strip()
    print(f'{corverde_final}', end='')
    
    idade = int(input(f'Idade: {corverde_inicio}'))
    print(f'{corverde_final}', end='')
    soma += idade
            
    sexo = str(input(f'Sexo [M/F]: {corverde_inicio}')).upper().strip()
    print(f'{corverde_final}', end='')
    
    if idade < 20 and sexo == 'F': # Se idade for menor do que 20 e for do sexo Feminino
        total_mulher_20 += 1 # Adicionar mais 1 ao acumulador

    if sexo == 'M': # Atualiza somente se for homem
        if idade > maior_idade:
            maior_idade = idade
            maior_idade_nome = nome

media_idade = soma / i # Média das idades

print(f'A média de idade do grupo é de {media_idade} anos.')
if maior_idade == -1:
    print('Nenhum homem foi registrado')
else:
    print(f'O homem mais velho tem {maior_idade} e se chama {maior_idade_nome}')
print(f'Ao todo são {total_mulher_20} mulheres com menos de 20 anos.')