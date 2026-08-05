class Pessoa:
    def __init__(self):
        self.nome = "Nívia"

p = Pessoa()

print(p.__nome)  #resultado da erro pq é um atributo protegido internamente