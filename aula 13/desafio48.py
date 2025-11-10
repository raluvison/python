soma = 0
cont = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'Dos {cont} valores o total é {soma}')
