import os

MAGENTA = "\033[95m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

pasta = r"C:\Users\1bmod\Documents\tt"

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

class SistemaCadastro:
    def __init__(self):
        self.clientes = []
        self.arquivo = "clientes.txt"
        self.carregar_clientes()

    def carregar_clientes(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(" | ")

                    nome = dados[0].replace("Nome: ", "")
                    idade = int(dados[1].replace("Idade: ", ""))
                    email = dados[2].replace("E-mail: ", "")
                    telefone = dados[3].replace("Telefone: ", "")

                    cliente = Cliente(nome, idade, email, telefone)
                    self.clientes.append(cliente)

        except FileNotFoundError:
            pass

    def cadastrar_cliente(self):
        try:
            print(MAGENTA + "\n---- CADASTRO ----" + RESET)

            while True:
                nome = input("Digite o nome: ").strip()

                if nome == "":
                    print(VERMELHO + "Nome não pode ser vazio." + RESET)

                elif nome.isnumeric():
                    print(VERMELHO + "Digite letras no nome." + RESET)

                else:
                    break

            while True:
                idade = input("Digite a idade: ").strip()

                if not idade.isnumeric():
                    print(VERMELHO + "Idade deve ser numérica." + RESET)

                else:
                    idade = int(idade)

                    if idade <= 0:
                        print(VERMELHO + "Idade inválida." + RESET)
                    else:
                        break

            while True:
                email = input("Digite o e-mail: ").strip().lower()

                if "@" not in email:
                    print(VERMELHO + "E-mail inválido." + RESET)
                else:
                    break

            while True:
                telefone = input("Digite o telefone: ").strip()

                telefone = telefone.replace(" ", "")

                if not telefone.isnumeric():
                    print(VERMELHO + "Telefone deve conter apenas números." + RESET)

                elif len(telefone) < 10:
                    print(VERMELHO + "Telefone deve possuir pelo menos 10 dígitos." + RESET)

                else:
                    break

            cliente = Cliente(nome, idade, email, telefone)

            self.clientes.append(cliente)

            self.salvar_arquivo(cliente)

            print(MAGENTA + "\nCliente cadastrado com sucesso!" + RESET)

        except Exception as erro:
            print(VERMELHO + f"Erro: {erro}" + RESET)

    def listar_clientes(self):

        if len(self.clientes) == 0:
            print(AMARELO + "\nNenhum cliente cadastrado." + RESET)

        else:
            print(MAGENTA + "\n---- CLIENTES ----" + RESET)

            for i, cliente in enumerate(self.clientes, start=1):

                print(
                    f"\nCliente {i}: "
                    f"Nome: {cliente.nome} | "
                    f"Idade: {cliente.idade} | "
                    f"E-mail: {cliente.email} | "
                    f"Telefone: {cliente.telefone}"
                )

    def editar_cliente(self):

        if len(self.clientes) == 0:
            print(AMARELO + "\nNenhum cliente cadastrado." + RESET)
            return

        self.listar_clientes()

        try:
            numero = int(
                input("\nDigite o número do cliente que deseja editar: ")
            )

            if numero < 1 or numero > len(self.clientes):
                print(VERMELHO + "Cliente não encontrado." + RESET)
                return

            cliente = self.clientes[numero - 1]

            print(MAGENTA + "\n---- EDITAR CLIENTE ----" + RESET)

            cliente.nome = input("Novo nome: ").strip()
            cliente.idade = int(input("Nova idade: "))
            cliente.email = input("Novo e-mail: ").strip()
            cliente.telefone = input("Novo telefone: ").strip()

            self.atualizar_arquivo()

            print(VERDE + "\nCliente atualizado com sucesso!" + RESET)

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
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Editar cliente")
            print("4 - Sair")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar_cliente()

            elif opcao == "2":
                self.listar_clientes()

            elif opcao == "3":
                self.editar_cliente()

            elif opcao == "4":

                while True:
                    confirmar = input(
                        "\nDeseja realmente sair? (s/n): "
                    ).strip().lower()

                    if confirmar == "s":
                        print(VERDE + "Sistema encerrado!" + RESET)
                        return

                    elif confirmar == "n":
                        break

                    else:
                        print(VERMELHO + "Digite apenas 's' ou 'n'." + RESET)

            else:
                print(VERMELHO + "Opção inválida." + RESET)


sistema = SistemaCadastro()

sistema.menu()