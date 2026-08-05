class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_dados(self):
        print(f"Produto nome: {self.nome}  | Produto preço: {self.preco}" )

prod1 = Produto("Teclado", 600)

prod1.exibir_dados()