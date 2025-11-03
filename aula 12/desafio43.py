altura = float(input('Digite seu altura: '))
peso = float(input('Digite sua peso: '))
imc = peso / (altura ** 2) 

print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc < 25:
    print('Você está com o PESO IDEAL!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')