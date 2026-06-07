import os
from colorama import Fore, Style, init

init()
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
            print(Fore.MAGENTA + "\n---- CADASTRO ----" + Style.RESET_ALL)

            while True:
                nome = input("Digite o nome: ").strip()

                if nome == "":
                    print(Fore.RED + "Nome não pode ser vazio." + Style.RESET_ALL)

                elif nome.isnumeric():
                    print(Fore.RED + "Digite letras no nome." + Style.RESET_ALL)

                else:
                    break

            while True:
                idade = input("Digite a idade: ").strip()

                if not idade.isnumeric():
                    print(Fore.RED + "Idade deve ser numérica." + Style.RESET_ALL)

                else:
                    idade = int(idade)

                    if idade <= 0:
                        print(Fore.RED + "Idade inválida." + Style.RESET_ALL)
                    else:
                        break

            while True:
                email = input("Digite o e-mail: ").strip().lower()

                if "@" not in email:
                    print(Fore.RED + "E-mail inválido." + Style.RESET_ALL)
                else:
                    break

            while True:
                telefone = input("Digite o telefone: ").strip()

                telefone = telefone.replace(" ", "")

                if not telefone.isnumeric():
                    print(Fore.RED + "Telefone deve conter apenas números." + Style.RESET_ALL)

                elif len(telefone) < 10:
                    print(Fore.RED + "Telefone deve possuir pelo menos 10 dígitos." + Style.RESET_ALL)

                else:
                    break

            cliente = Cliente(nome, idade, email, telefone)

            self.clientes.append(cliente)

            self.salvar_arquivo(cliente)

            print(Fore.MAGENTA + "\nCliente cadastrado com sucesso!" + Style.RESET_ALL)

        except Exception as erro:
            print(Fore.RED + f"Erro: {erro}" + Style.RESET_ALL)

    def listar_clientes(self):

        if len(self.clientes) == 0:
            print(Fore.YELLOW + "\nNenhum cliente cadastrado." + Style.RESET_ALL)

        else:
            print(Fore.MAGENTA + "\n---- CLIENTES ----" + Style.RESET_ALL)

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
            print(Fore.YELLOW + "\nNenhum cliente cadastrado." + Style.RESET_ALL)
            return

        self.listar_clientes()

        try:
            numero = int(
                input("\nDigite o número do cliente que deseja editar: ")
            )

            if numero < 1 or numero > len(self.clientes):
                print(Fore.RED + "Cliente não encontrado." + Style.RESET_ALL)
                return

            cliente = self.clientes[numero - 1]

            print(Fore.MAGENTA + "\n---- EDITAR CLIENTE ----" + Style.RESET_ALL)

            cliente.nome = input("Novo nome: ").strip()
            cliente.idade = int(input("Nova idade: "))
            cliente.email = input("Novo e-mail: ").strip()
            cliente.telefone = input("Novo telefone: ").strip()

            self.atualizar_arquivo()

            print(Fore.GREEN + "\nCliente atualizado com sucesso!" + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "\nDigite valores válidos." + Style.RESET_ALL)

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

            print(Fore.MAGENTA + "\n---- MENU PRINCIPAL ----" + Style.RESET_ALL)
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
                        print(Fore.GREEN + "Sistema encerrado!" + Style.RESET_ALL)
                        return

                    elif confirmar == "n":
                        break

                    else:
                        print(Fore.RED + "Digite apenas 's' ou 'n'." + Style.RESET_ALL)

            else:
                print(Fore.RED + "Opção inválida." + Style.RESET_ALL)


sistema = SistemaCadastro()

sistema.menu()