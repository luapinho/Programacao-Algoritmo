class Pessoa: #Superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá! Sou o {self.nome} e minha idade é {self.idade}")

class Aluno(Pessoa): #parte da herança , Subclasse
    def estudar(self):
        print("Estudante...")

a1 = Aluno("JOÃO", 17)
a1.falar()
a1.estudar()