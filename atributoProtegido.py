class Pessoa:
    def __init__(self):
        self._nome = "Gnomo"

p = Pessoa()

print(p._nome) #self._nome é "uso interno da classe"