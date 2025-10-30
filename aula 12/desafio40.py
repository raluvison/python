nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2


print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')

if media >= 7:
    print('O aluno foi APROVADO!')
elif 5 <= media < 7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')