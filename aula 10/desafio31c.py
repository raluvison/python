distance = float(input('Digite a distância da viagem em Km: '))
valor = distance * 0.50 if distance < 200 else distance * 0.45
print(f'O preço da passagem numa viagem de {distance}Km é de: R${valor:.2f}')