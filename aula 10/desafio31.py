distance = int(input('Digite a distância da viagem em Km: '))

if distance < 200:
    passagem1 = distance * 0.50
    print(f'O preço da passagem numa viagem de {distance}Km é de: R${passagem1:.2f}')
else:
    passagem2 = distance * 0.45
    print(f'O preço da passagem numa viagem de {distance}Km é de: R${passagem2:.2f}')