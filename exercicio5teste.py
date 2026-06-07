produtos = []

def cadastrar_produto():
    try:
        # strip() remove espaços antes e depois
            nome = input("Digite o nome do produto: ").strip()

        # isnumeric() verifica se foi digitado apenas números
            if nome.isnumeric():
                print("Erro: digite letras no nome.")
                return
        
            preco = input("Digite o preço do produto: R$ ").strip().replace(",", ".")

            preco = float(preco)

        # [nome, preco] cria uma lista com nome e preço
            produtos.append([nome, preco])
            print("Produto cadastrado com sucesso!")

    # Caso o usuário digite preço inválido
    except ValueError:
        print("Digite um preço válido.")

def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")

    else:
        print("\n----LISTA DE PRODUTOS----")

        # enumerate() percorre a lista
        # start=1 faz começar do número 1
        for i, produto in enumerate(produtos, start=1):

            # produto[0] pega o nome
            # produto[1] pega o preço
            print(f"Produto {i}: {produto[0]} | R${produto[1]:.2f}")

def comprar_produto():
    try:
        if len(produtos) == 0:
            print("Não há produtos cadastrados.")
            return

        # Chama a função listar_produtos()
        listar_produtos()

        indice = int(input("\nDigite o número do produto: ").strip())

        # Como a lista começa do 0,
        # subtrai 1 do número digitado
        indice = indice - 1

        if indice < 0 or indice >= len(produtos):
            print("Produto inexistente.")
            return
        
        quantidade = int(input("Digite a quantidade: ").strip())

        # Guarda o produto escolhido
        produto = produtos[indice]

        total = produto[1] * quantidade

        print(f"\nProduto escolhido: {produto[0]}")

        print(f"Total a pagar: R${total:.2f}")

        if total >= 100:

            print("Desconto disponível!")

        else:

            print("Sem desconto.")

    # Caso o usuário digite letras no lugar de números
    except ValueError:
        print("Digite apenas números válidos.")

while True:

    print("\n----MENU----")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        comprar_produto()

    elif opcao == "4":
        print("Encerrando o programa...")
        while True:
            opcao_final = input("Tem certeza que deseja sair: (s/n) ").strip().lower()

            if opcao_final == "s" or opcao_final == "n":
                break
            else:
                print("Digite apenas 's' ou 'n'.")
        if opcao_final == "s":
            print("Programa realmente encerrado!")
            break

    else:
        print("Opção inválida.")