produtos = []

quantidade_produtos = int(input("Quantos produtos serão cadastrados: "))

for i in range(quantidade_produtos):
    print(f"\nProduto {i+1}")
    nome_do_produto = input("Nome: ").capitalize()
    preco_produto = float(input("Preço: ")).replace(",", ".")
    quantidade_estoque = int(input("Quantidade em estoque: "))
    
    produto = {
    "nome" : nome_do_produto,
    "preco" : preco_produto,
    "estoque" : quantidade_estoque
    }

    produtos.append(produto)

    
while True:
    nome_do_cliente = input("\nNome do cliente: ")
    
    total = 0
    carrinho = []
        
    while True:
        nome_prod = input("Digite o nome do produto desejado(ou 'fim para encerrar): ")
            
        if nome_prod == "fim":
            break
            
        encontrado = None   
        for p in produtos:
            if p["nome"].lower() == nome_prod.lower():
                encontrado = p
                break
                
        if encontrado is None:
            print("Produto não encontrado")
            continue
                
        quantidade_desejada = int(input("Digite a quantidade de produto desejada:"))
                
        if quantidade_desejada > encontrado["estoque"]:
            print("Estoque insuficiente!")
            continue
        
        subtotal = quantidade_desejada * encontrado["preco"]
        total += subtotal
        encontrado["estoque"] -= quantidade_desejada

        carrinho.append({
            "produto": encontrado["nome"],  
            "quantidade": quantidade_desejada,
            "subtotal": subtotal
        })


        print(f"Subtotal: R$ {subtotal:.2f}")     
        
        
    def desconto(total):
        if total >= 1000:
            return total * 0.15
        elif total >= 500 and 1000:
            return total * 0.10
        elif total >= 200 and 500:
            return total * 0.05
        else:
            return 0
    
    valor_desconto = desconto(total)
    total_final = total - valor_desconto
    
    print("Cliente: ", nome_do_cliente)

    print ("\nProdutos comprados:")
    for item in carrinho:
        print(f"{item['produto']} - {item['quantidade']}x - R$ {item['subtotal']:.2f}")
        
    print("\nTotal da compra: ", total)
    print("Desconto: ", valor_desconto)
    print("Total final: ", total_final)  
        
    continuar = input("\nDeseja realizar outra venda? (s/n ): ")
    if continuar.lower() == "n":
        break
        
print("\nPrograma encerrado , obrigado pela preferencia de compra com a gente.")