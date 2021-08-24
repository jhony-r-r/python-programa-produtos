codigos = []
nomes = []
marcas = []
modelos = []
valores = []
quantidades = []
produtos = []
depto = []

departamentos = ["Monitor", "Cadeira", "Hardware", "Periféricos", "Gabinete"]
nDepartamentos = [1, 2, 3, 4, 5, 6, 7]

colunas = ["Código:", "Nome:", "Marca:", "Modelo:", "Valor:", "Quantidade:"]

requisitos = {
    "codigo": "digite o código do produto: ".capitalize(),
    "nome": "digite o nome do produto: ".capitalize(),
    "marca": "digite a marca do produto: ".capitalize(),
    "modelo": "digite o modelo do produto: ".capitalize(),
    "valor": "digite o valor do produto: ".capitalize(),
    "qtd": "digite a quantidade do produto: ".capitalize()
}

questionamento = str(input("Deseja cadastrar um produto (sim/não)? "))

while questionamento == 'SIM' or questionamento == 'Sim' or questionamento == 'S' or questionamento == 's' or questionamento == 'sim':
    print('-'*100)
    print('DEPARTAMENTOS')
    print('-'*100)

    for i in range(0, 5):
        print('[{}] {}'.format(nDepartamentos[i], departamentos[i]))

    print('')
    dSelecionado = int(
        input('Escolha o departamento conforme sua numeração: '))

    msg_dep_sel = 'Departamento selecionado pelo usuário é'

    if dSelecionado == 1:
        print('-'*100)
        print('{} {}'.format(msg_dep_sel, departamentos[0]))
        print('-'*100)
        codigo = int(input(requisitos.get("codigo")))
        nome = str(input(requisitos.get("nome")))
        marca = str(input(requisitos.get("marca")))
        modelo = str(input(requisitos.get("modelo")))
        valor = float(input(requisitos.get("valor")))
        qtd = int(input(requisitos.get("qtd")))

        codigos.append(codigo)
        nomes.append(nome)
        marcas.append(marca)
        modelos.append(modelo)
        valores.append(valor)
        quantidades.append(qtd)
        depto.append(departamentos[0])

        if codigo != 0 and nome != '' and marca != '' and modelo != '' and valor > 0 and qtd > 0:

            questionamento = str(
                input("Deseja cadastrar um novo produto (sim/não)? "))

            produtos = [codigo, nome, marca, modelo, valor, qtd]

        print('-'*100)
        print('{}'.format('Último produto cadastrado:'.upper()))
        for i in range(6):
            print(colunas[i], produtos[i])
        print('-'*100)

    elif dSelecionado == 2:
        print('-'*100)
        print('{} {}'.format(msg_dep_sel, departamentos[1]))
        print('-'*100)
        codigo = int(input(requisitos.get("codigo")))
        nome = str(input(requisitos.get("nome")))
        marca = str(input(requisitos.get("marca")))
        modelo = str(input(requisitos.get("modelo")))
        valor = float(input(requisitos.get("valor")))
        qtd = int(input(requisitos.get("qtd")))

        codigos.append(codigo)
        nomes.append(nome)
        marcas.append(marca)
        modelos.append(modelo)
        valores.append(valor)
        quantidades.append(qtd)
        depto.append(departamentos[1])

        if codigo != 0 and nome != '' and marca != '' and modelo != '' and valor > 0 and qtd > 0:

            questionamento = str(
                input("Deseja cadastrar um novo produto (sim/não)? "))

            produtos = [codigo, nome, marca, modelo, valor, qtd]

        print('-'*100)
        print('{}'.format('Último produto cadastrado:'.upper()))
        for i in range(6):
            print(colunas[i], produtos[i])
        print('-'*100)

    elif dSelecionado == 3:
        print('-'*100)
        print('{} {}'.format(msg_dep_sel, departamentos[2]))
        print('-'*100)
        codigo = int(input(requisitos.get("codigo")))
        nome = str(input(requisitos.get("nome")))
        marca = str(input(requisitos.get("marca")))
        modelo = str(input(requisitos.get("modelo")))
        valor = float(input(requisitos.get("valor")))
        qtd = int(input(requisitos.get("qtd")))

        codigos.append(codigo)
        nomes.append(nome)
        marcas.append(marca)
        modelos.append(modelo)
        valores.append(valor)
        quantidades.append(qtd)
        depto.append(departamentos[2])

        if codigo != 0 and nome != '' and marca != '' and modelo != '' and valor > 0 and qtd > 0:

            questionamento = str(
                input("Deseja cadastrar um novo produto (sim/não)? "))

            produtos = [codigo, nome, marca, modelo, valor, qtd]
        
        print('-'*100)
        print('Ultimo produto cadastrado:')
        for i in range(6):
            print(colunas[i], produtos[i])
        print('-'*100)

    elif dSelecionado == 4:
        print('-'*100)
        print('{} {}'.format(msg_dep_sel, departamentos[3]))
        print('-'*100)
        codigo = int(input(requisitos.get("codigo")))
        nome = str(input(requisitos.get("nome")))
        marca = str(input(requisitos.get("marca")))
        modelo = str(input(requisitos.get("modelo")))
        valor = float(input(requisitos.get("valor")))
        qtd = int(input(requisitos.get("qtd")))

        codigos.append(codigo)
        nomes.append(nome)
        marcas.append(marca)
        modelos.append(modelo)
        valores.append(valor)
        quantidades.append(qtd)
        depto.append(departamentos[3])

        if codigo != 0 and nome != '' and marca != '' and modelo != '' and valor > 0 and qtd > 0:

            questionamento = str(
                input("Deseja cadastrar um novo produto (sim/não)? "))

            produtos = [codigo, nome, marca, modelo, valor, qtd]

        print('-'*100)
        for i in range(6):
            print(colunas[i], produtos[i])
        print('-'*100)

    elif dSelecionado == 5:
        print('-'*100)
        print('{} {}'.format(msg_dep_sel, departamentos[4]))
        print('-'*100)
        codigo = int(input(requisitos.get("codigo")))
        nome = str(input(requisitos.get("nome")))
        marca = str(input(requisitos.get("marca")))
        modelo = str(input(requisitos.get("modelo")))
        valor = float(input(requisitos.get("valor")))
        qtd = int(input(requisitos.get("qtd")))

        codigos.append(codigo)
        nomes.append(nome)
        marcas.append(marca)
        modelos.append(modelo)
        valores.append(valor)
        quantidades.append(qtd)
        depto.append(departamentos[4])

        if codigo != 0 and nome != '' and marca != '' and modelo != '' and valor > 0 and qtd > 0:

            questionamento = str(
                input("Deseja cadastrar um novo produto (sim/não)? "))

            produtos = [codigo, nome, marca, modelo, valor, qtd]

        print('-'*100)
        print('Ultimo produto cadastrado:')
        for i in range(6):
            print(colunas[i], produtos[i])
        print('-'*100)

    else:
        print('Selecione uma opção válida !')

else:
    print('-'*100)
    print('LISTAGEM DE PRODUTOS CADASTRADOS')
    print('-'*100)
    for i in range(len(depto and codigos and nomes and marcas and modelos and valores and quantidades)):
        print('{} {} {} {} {} R${:.2f} {}'.format(
            depto[i], codigos[i], nomes[i], marcas[i], modelos[i], valores[i], quantidades[i]))
        print('-'*100)
