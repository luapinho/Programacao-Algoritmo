#funçoes

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco= preco



Produtos = [] #lista

while True:
    print("\n---Cadrasto de produtos---")
    nome = input("Nome do produto: ")

    while True:
        preco = float(input("Preço do produto: ")).strip().replace(",", ".")

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
    Produtos.append(produto) #adiciona o produto na lista
    
    while True:
        nome_do_cliente = input("\nNome do cliente: ")


        quantidade = int(input("Quantidade desejada: "))

    
