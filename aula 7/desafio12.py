print('Irei aplicar um desconto de 5% sobre o valor do produto.')
val = float(input('Me diga o valor do produto: R$'))
des = val * 0.05
som = val - des

print(f'O valor do produto passou de R${val} para R${som:.2f} aplicando 5% de desconto!')
