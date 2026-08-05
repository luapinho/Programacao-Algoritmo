class Animal:
    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("AUAU!")

class Gato(Animal):
    def emitir_som(self):
        print("MIAU!")

class Vaca(Animal):
    def emitir_som(self):
        print("MUUU!")

animais = [Cachorro(), Gato(), Vaca(), Animal()]

for a in animais:
    a.emitir_som()