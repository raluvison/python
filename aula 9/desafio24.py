nome = input('Digite o nome da sua cidade: ').strip()

print(f'Ela começa com a frase SANTO? {nome.upper()[:5] == 'SANTO'}')