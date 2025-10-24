print('Me diga 3 retas que irei dizer se podem formar um triângulo!')
r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Ele pode formar um triângulo!')
else:
    print('Ele não pode formar um triângulo!')