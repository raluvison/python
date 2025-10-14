#CRIAR UM FILTRO DE CATEGORIA QUE MOSTRE OS PRODUTOS E OS VALORES DELA

pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"), #exemplo de tupla
    ("Calça", "Vestuário", 79.90, "Pendente"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Fone de ouvido", "Eletrônicos", 129.90, "Entregue"),
    ("Meia", "Vestuário", 49.90, "Entregue"),
    ("Relógio", "Acessórios", 499.90, "Pendente"),
    #Posições de elementos dentro da lista("0", "1", "2", "3")
]

filtro = input("Digite a categoria que você deseja: ")

for i in pedidos: #para cada item dentro da lista pedidos, estrutura de laço
    if filtro == i[1]:
        print(f'Pedido: {i[0]} ------- Valor (R$): {i[2]} ------- Situação: {i[3]}'.center(40))