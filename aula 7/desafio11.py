print('Vamos calcular a área da sua parede quantos litros de tinta será necessário para pintá-la. Cada litro de tinta pinta 2m²')
l = int(input('Me diga a largura da parede: '))
a = int(input('Me diga a altura da parede: '))
area = l * a
tinta = area / 2

print(f'A área da parede é de: {area}m². Serão utilizados {tinta}l de tinta')