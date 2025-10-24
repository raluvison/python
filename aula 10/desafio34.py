salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    aumento1 = (salario * 0.1) + salario
    print(f'Com 10% de aumento seu salário subiu para: R${aumento1:.2f}')
else:
    aumento2 = (salario * 0.15) + salario
    print(f'Com 15% de aumento seu salário subiu para: R${aumento2:.2f}')