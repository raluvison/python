n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2

print(f'Sua média foi: {media:.1f}')
if media >= 8.0:
    print('Parabéns! Você foi acima da média.')
else:
    print('Sua média foi normal')