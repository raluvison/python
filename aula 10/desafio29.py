vel = int(input('Digite a velocidade que você passou no radar: '))
multa = (vel-80)*7
if vel >= 80:
    print(f'Você foi multado! A multa ficou no valor de: R${multa:.2f}')
print(f'Velocidade medida: {vel}Km/h\nTenha um ótimo dia!')