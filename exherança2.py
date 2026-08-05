class Pessoa:
   def __init__(self, nome, idade):
           self.nome = nome
           self.idade = idade
   
    def falar(self):
        print(f"Olá! Sou o {self.nome} e minha idade é {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome,idade,curso):
          super().__init__(nome, idade)
          self.curso = curso

    def estudar(self):
         print(f"Estou estudando {self.curso}")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
          super().__init__(nome, idade)
          self.disciplina = disciplina

    def ensinar(self):
         print(f"Estou ensinando {self.disciplina}")


a1 = Pessoa("Julia", 60)
a1.falar()
a2 = Aluno("Guilherme", 14, "Administraçaõ")
a2.estudar()
a2.estudar()
a3 = Professor("Marcos", 45, "Matemática")
a3.falar()
a3.ensinar()
