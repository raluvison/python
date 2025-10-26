distance = float(input('Digite a distância da viagem em Km: '))

if distance < 200:
    preço = distance * 0.50
else:
    preço = distance * 0.45
print(f'O preço da passagem numa viagem de {distance}Km é de: R${preço:.2f}')