import os
pasta = r"C:\Users\1bmod\Documents\tt"

class Cliente:
    # __init__ recebe os dados do cliente
    def __init__(self, nome, idade, email, telefone):

        # self salva os dados dentro do objeto
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
            print("\n---- CADASTRO ----")

            while True:
                nome = input("Digite o nome: ").strip()

                if nome == "":
                    print("Nome não pode ser vazio.")

                elif nome.isnumeric():
                    print("Digite letras no nome.")

                else:
                    break

            while True:
                idade = input("Digite a idade: ").strip()

                if not idade.isnumeric():
                    print("Idade deve ser numérica.")

                else:
                    idade = int(idade)

                    if idade <= 0:
                        print("Idade inválida.")
                    else:
                        break

            while True:
                email = input("Digite o e-mail: ").strip().lower()

                if "@" not in email:
                    print("E-mail inválido.")
                else:
                    break

            while True:
                telefone = input("Digite o telefone: ").strip()

                telefone = telefone.replace(" ", "")

                if not telefone.isnumeric():
                    print("Telefone deve conter apenas números.")

                elif len(telefone) < 10:
                    print("Telefone deve possuir pelo menos 10 dígitos.")

                else:
                    break

            # Cria objeto cliente
            cliente = Cliente(nome, idade, email, telefone)

            self.clientes.append(cliente)

            self.salvar_arquivo(cliente)

            print("\nCliente cadastrado com sucesso!")

        except Exception as erro:
            print("Erro:", erro)

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("\nNenhum cliente cadastrado.")
        else:
            print("\n---- CLIENTES ----")

            # enumerate() numera os itens
            for i, cliente in enumerate(self.clientes, start=1):
                print(
                    f"\nCliente {i} : Nome: {cliente.nome} | Idade: {cliente.idade} | E-mail: {cliente.email} | Telefone: {cliente.telefone} ")

    def salvar_arquivo(self, cliente):

        # Abre o arquivo em modo adicionar
        with open(self.arquivo, "a", encoding="utf-8") as arquivo:

            arquivo.write(
                f"Nome: {cliente.nome} | "
                f"Idade: {cliente.idade} | "
                f"E-mail: {cliente.email} | "
                f"Telefone: {cliente.telefone}\n"
            )

    def menu(self):
        while True:

            print("\n---- MENU PRINCIPAL ----")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Sair")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar_cliente()

            elif opcao == "2":
                self.listar_clientes()

            elif opcao == "3":

                while True:
                    confirmar = input(
                        "\nDeseja realmente sair? (s/n): "
                    ).strip().lower()

                    if confirmar == "s":
                        print("Sistema encerrado!")
                        return

                    elif confirmar == "n":
                        break

                    else:
                        print("Digite apenas 's' ou 'n'.")

            else:
                print("Opção inválida.")


# Cria objeto do sistema
sistema = SistemaCadastro()

# Inicia o programa
sistema.menu()