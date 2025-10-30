from InquirerPy import prompt

while True:
    conhecimento = [
        {
            "type": "list",
            "name": "nivel",
            "message": "Qual seu conhecimento Python?",
            "choices": ["Iniciante", "Intermediário", "Avançado"]
        },
    ]

    resultados = prompt(conhecimento)
    nivel = resultados["nivel"]

    if nivel == "Iniciante":
        print('Boa sorte na sua jornada aprendendo Python!')
    elif nivel == "Intermediário":
        print('Você está no caminho certo!')
    elif nivel == "Avançado":
        print('Oloco ai você já chegou no nível do gabinho.')

    pergunta = [
        {
            'type': 'list',
            'name': 'escolha',
            'message': 'Você deseja tentar de novo?',
            'choices': ['Sim', 'Não']
        },
    ]

    escolhas = prompt(pergunta)
    escolha = escolhas['escolha']

    if escolha == 'Não':
        break
    else:
        print('')