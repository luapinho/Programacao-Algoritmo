#funçoes
def calcular_subtotal(preco, quantidade): #criando uma função para calcular
    return preco * quantidade 


def desconto(total): # criou uma função para desconto,return é o que vai retornar
    if total >= 1000: #uma condição se for certo executa o return,15% de desconto
        return total * 0.85 
    elif total >= 500: #10% de desconto
        return total * 0.90
    elif total >= 200: #5% de desconto
        return total * 0.95
    else:
        return total


def calcular_media(total,quantidade):
    if quantidade == 0: # evita erro, se declararmos que é 0,pq dividir por 0 da erro
        return 0
    return total / quantidade 


def maior_compra(vendas): # criando uma função para encontrar qual cliente gastou mais
    maior = vendas[0] # precisa começar com algum valor, ta declarando que a primeira venda é a maior
    for v in vendas: #percorre todas as vendas
        if v["total da compra"] > maior["total da compra"]: #comparando os valores
            maior = v #atualiza se encontrar uma maior,a variavel
    return maior


# Cadastro de produtos
produtos = [] #lista onde todos os produtos serão armazenados

while True:
    print("\n---Cadrasto de produtos---")
    nome = input("Nome do produto: ")

    while True:
        preco = float(input("Preço do produto: "))

        if preco >=0:
            break
        else:
            print("Digite um preço válido.")

    while True:
        estoque = int(input("Estoque do produto: "))

        if estoque >=0:
            break
        else:
            print("Digite um valor válido.")

    produto = {  #criando um dicionário com os dados da lista
        "nome": nome,
        "preco": preco,
        "estoque": estoque
}
    produtos.append(produto) #adiciona o produto na lista


    while True:
        continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()
        if continuar == 's' or continuar == 'n' :  #se digitar n para o programa,e lower ajuda  
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    if continuar == 'n':
        break
        
vendas = []  #lista para guardar todas as vendas
        
while True:
    nome_cliente = input("\nNome do cliente: ")
    total = 0 #começa o total da compra zerado
    print("\nProdutos disponíveis:")
    for p in produtos: #percorre todos os produtos cadastrados
        print(f"{p['nome']} | R$ {p['preco']:.2f} | estoque: {p['estoque']}")
    

    while True:
        nom_produto = input("\nQual produto deseja comprar: ")
            
        encontrado = None #none:nenhum valor,ele inicia vazio

        for p in produtos: #procura o produto pelo nome,é o jeito mais facil de percorrer listas
            if p["nome"].lower() == nom_produto.lower():
                encontrado = p #vai guardar produto encontrado
                break

        if encontrado is None: #se não encontrou o produto
            print("Produto não encontrado!")
            continue #volta pro início do loop 

        quantidade = int(input("Quantidade desejada: "))

        if quantidade > encontrado["estoque"]:
            print("Estoque insuficiente!")
            continue

        subtotal = calcular_subtotal(encontrado["preco"], quantidade)
        total += subtotal
        encontrado["estoque"] -= quantidade #diminui no estoque

        print(f"Subtotal: R$ {subtotal:.2f}")

        while True:
            continuar = input("Deseja adicionar mais produtos? (s/n): ").lower()
            if continuar == 's' or continuar == 'n':
                break
            else:
                print("Digite apenas 's' ou 'n'.")

        if continuar == 'n':
            break

    #Finaliza a compra
    total_final = desconto(total) #ta chamando a funçao
        
    vendas.append({
    "cliente": nome_cliente,
    "total da compra": total_final
})
        
    print(f"Total com desconto: R$ {total_final:.2f}")

    while True:
        continuar = input("\nDeseja realizar uma nova venda? (s/n): ").lower().replace(",", ".")
        if continuar == 's' or continuar == 'n' :  #se digitar n para o programa,e lower ajuda  
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    if continuar == 'n':
        break
        

# Relatório final
total_vendas = len(vendas) #quantidade de vendas
totais = []
for v in vendas:
    totais.append(v["Total da compra"])

faturamento = sum(totais) #soma de todo dinheiro ganho

print(f"\nTotal de vendas: {total_vendas}")
print(f"Faturamento: R$ {faturamento:.2f}")

if vendas: #verificando se existe alguma venda
    maior = maior_compra(vendas) 
    print(f"Maior compra: {maior['cliente']} (R$ {maior['total da compra']:.2f})") #ta mostrando o maior cliente e o total da compra

media = calcular_media(total,quantidade)
print(f"Média das vendas: R$ {media:.2f}") 
    
print("\nPrograma encerrado.")