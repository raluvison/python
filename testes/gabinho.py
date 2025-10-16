nome = input('Digite o seu nome completo: ')
separado = nome.split()

print(
    f'Nome completo: {nome} \n'
    f'Primeiro nome: {separado[0]} \n'
    f'Ultimo sobrenome: {separado[len(separado) - 1]}'
)

class Nome():
    def __init__(self, nome):
        self.nome = nome
        self.separado = nome.split()

    def primeiro_nome(self):
        primeiro_nome = self.separado[0]
        return primeiro_nome
    
    def sobrenome(self):
        sobrenome = self.separado[self.busca_ultimo_indice()]

    def busca_ultimo_indice(self):
        contagem_lista = len(self.separado) 
        indice = contagem_lista - 1
        return indice