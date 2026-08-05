class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco 

    def mostrar(self):
        print(f"Produto: {self.nome} | Preço: {self.preco}")

p1 = Produto("Mouse", 50)
p1.mostrar()