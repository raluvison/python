nome = input('Digite o nome da sua cidade: ').strip()

print(f'Ela começa com a frase SANTO? {nome.title()[:5] == 'Santo'}')