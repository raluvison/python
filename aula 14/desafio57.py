s = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]

while s not in 'MmFf':
    s = str(input('Dados inválidos! Digite novamente seu sexo: [M/F] ')).upper().strip()[0]
print(f'Seu sexo é {s}')