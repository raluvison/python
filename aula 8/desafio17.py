from math import pow, sqrt

co = float(input('Diga o valor do cateto oposto: '))
ca = float(input('Diga o valor do cateto adjacente: '))
sc = pow(co, 2) + pow(ca, 2) 
hip = sqrt(sc)

print(f'O triângulo retângulo com o cateto oposto de {co} e o cateto adjacente de {ca} resulta na hipotenusa de {hip:.1f}.')