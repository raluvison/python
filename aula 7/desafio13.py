print('Fale o salário de um funcionário que ele irá ganhar 15% de aumento')
sal = float(input('Salário: R$'))
aum = sal * 0.15
total = sal + aum

print(f'Seu salário aumentou de R${sal:.2f} para R${total:.2f}!')