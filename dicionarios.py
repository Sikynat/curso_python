print('Controle de estoque')

estoque = {
    'Café Terreiro 500g': {'valor': 25.95, 'quantidade': 23},
    'Arroz Tio João 1kg': {'valor': 8.90, 'quantidade': 50},
    'Feijão Carioca 1kg': {'valor': 6.50, 'quantidade': 30}
}

while True:
    print('1 - Visualizar Estoque Atual')
    print('2 - Registrar Entrada de Produto')
    print('3 - Registrar Saída de Produto')
    print('4 - Sair do Sistema')

    resposta = input('O que deseja fazer: ')

    if resposta == "1":
        for c, v in estoque.items():
            print(f'{c} - Quantidade: {v["quantidade"]} - Valor: R${v["valor"]}')
    elif resposta == "2":
        nome_produto = input('Nome do produto: ')
        if nome_produto in estoque:
            quantidade = int(input('Quantidade a adicionar: '))
            estoque[nome_produto]['quantidade'] += quantidade
        else:
            print('Produto não encontrado.')
    elif resposta == "4":
        break
print('Fim.')