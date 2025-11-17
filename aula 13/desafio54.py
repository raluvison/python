from datetime import date

ano_atual = date.today().year
cont_menor = 0
cont_maior = 0

for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}° pessoa nasceu? '))
    idade = ano_atual - ano
    
    if idade < 18:
        cont_menor += 1
    else:
        cont_maior += 1

print(f'Ao todo tivemos {cont_maior} maiores de idade')
print(f'E também tivemos {cont_menor} menores de idade.')
