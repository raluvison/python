soma = 0
contador = 0

for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        contador += +1
print(f'A soma dos {contador} números PARES digitados é {soma}')