import os

MAGENTA = "\033[95m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

pasta = r"C:\Users\1bmod\Documents\tt"

class Aluno:
    def __init__(self, nome, idade, nota, indice):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.indice = indice

    def mostrarAlunos(self):
        print(f"{self.indice} : NOME: {self.nome} | IDADE: {self.idade} | NOTA: {self.nota}")

Alunos = []

class cadastro():
    def cadastro(Alunos):
        print("====CADASTRO====")
        while True:
                nome = input("Digite o nome do aluno.").strip()

                if nome == "":
                    print(VERMELHO + "Nome não pode ser vazio." + RESET)

                elif nome.isnumeric():
                    print(VERMELHO + "Digite letras no nome." + RESET)

                else:
                    break

        while True:
            try:
                idade = int(input("Digite a idade do aluno.")).strip()

                if idade <= 0:
                        print(VERMELHO + "Idade inválida." + RESET)

                elif not idade.isnumeric():
                    print(VERMELHO + "Idade deve ser numérica." + RESET)

                else:
                     break
                
            except ValueError:
                print(VERMELHO + "Digite novamente" + RESET)

        while True:
            try:
                 nota = int(input("Digite a nota do aluno: ").strip())
                 if nota < 0 or nota >10:
                    print(VERMELHO + "A nota não pode ser menor do que '0' nem maior do que '10'!" + RESET)
                    break
            except:
                print(VERMELHO + "Apenas números" + RESET)
        
        print(VERDE + "Cadastrado com sucesso!" + RESET)

def listar_Alunos(self):
        with open(pasta, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        if len(self.aluno) == 0:
            print(AMARELO + "\nNenhum aluno cadastrado." + RESET)

        else:
            print(MAGENTA + "\n---- ALUNOS ----" + RESET)

            for i, Alunos in enumerate(self.alunos, start=1):

                print(
                    f"\nAlunos {i}: "
                    f"Nome: {Alunos.nome} | "
                    f"Idade: {Alunos.idade} | "
                    f"Nota: {Alunos.nota} | "
                )

def editar_alunos(self):

        if len(self.alunos) == 0:
            print(AMARELO + "\nNenhum alunos cadastrado." + RESET)
            return

        self.listar_clientes()

        try:
            numero = int(
                input("\nDigite o número do aluno que deseja editar: ")
            )

            if numero < 1 or numero > len(self.alunos):
                print(VERMELHO + "Aluno não encontrado." + RESET)
                return

            Aluno = self.aluno[numero - 1]

            print(MAGENTA + "\n---- EDITAR Aluno ----" + RESET)

            Aluno.nome = input("Novo nome: ").strip()
            Aluno.idade = int(input("Nova idade: "))
            Aluno.email = input("Novo e-mail: ").strip()
            Aluno.telefone = input("Novo telefone: ").strip()

            self.atualizar_arquivo()

            print(VERDE + "\nAluno atualizado com sucesso!" + RESET)

        except ValueError:
            print(VERMELHO + "\nDigite valores válidos." + RESET)

        def salvar_arquivo(self, cliente):

        with open(self.arquivo, "a", encoding="utf-8") as arquivo:

            arquivo.write(
                f"Nome: {cliente.nome} | "
                f"Idade: {cliente.idade} | "
                f"E-mail: {cliente.email} | "
                f"Telefone: {cliente.telefone}\n"
            )

    def atualizar_arquivo(self):

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            for cliente in self.clientes:

                arquivo.write(
                    f"Nome: {cliente.nome} | "
                    f"Idade: {cliente.idade} | "
                    f"E-mail: {cliente.email} | "
                    f"Telefone: {cliente.telefone}\n"
                )

        def menu(self):
            while True:
                print(MAGENTA + "\n---- MENU PRINCIPAL ----" + RESET)
                print("1 - Cadastrar Alunos")
                print("2 - Listar Alunos")
                print("3 - Editar Alunos")
                print("4 - Sair")

                opcao = input("\nEscolha uma opção: ").strip()

                if opcao == "1":
                    self.cadastrar_alunos()

                elif opcao == "2":
                    self.listar_alunos()

                elif opcao == "3":
                    self.editar_alunos()

                elif opcao == "4":

                    while True:
                        confirmar = input("\nDeseja realmente sair? (s/n): ").strip().lower()
                        if confirmar == "s":
                            print(VERDE + "Sistema encerrado!" + RESET)
                            return

                        elif confirmar == "n":
                            break

                        else:
                            print(VERMELHO + "Digite apenas 's' ou 'n'." + RESET)

                else:
                    print(VERMELHO + "Opção inválida." + RESET)

sistema = cadastro()

sistema.menu() 