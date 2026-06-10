import os
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
LIGHT_BLUE = "\033[94m"
RESET = "\033[0m"

ARQUIVO = r"C:\Users\1bmod\Documents\tt"

lista_alunos = []
class Aluno():
    def __init__(self, nome, idade, nota, indice):
        self.nome = nome  
        self.idade = idade
        self.nota = nota
        self.indice = indice
        
    def mostrardados(self):
        print(f'{self.indice}- Nome:{self.nome} | idade:{self.idade} | Nota:{self.nota}')
        
        
class SistemaCadastro():
    @staticmethod
    def cadastro(lista_alunos):   
        print("----------CADASTRO------------\n")
        nome = input("Digite o nome do aluno: ").strip().lower()
        while nome == "":
            print(f"\n{RED}O nome não pode ser vazio!{RESET}")
            nome = input("Digite o nome do aluno: ").strip().lower()
        while True:
            try:    
                idade = int(input("Digite a idade do aluno: ").strip())
                while idade <= 0:
                    print(f"\n{RED}A idade não pode ser menor do que zero!{RESET}")
                    idade = int(input("Digite a idade do aluno: ").strip())
                break
            except ValueError:
                print( f"\n{RED}Digite apenas números{RESET}")
        try:        
            nota = int(input("Digite a nota do aluno: ").strip())
            while nota < 0 or nota >10:
                print(f"\n{RED}A nota não pode ser menor do que '0' nem maior do que '10'!{RESET}")
                nota = int(input("Digite a nota do aluno: ").strip())
                break
        except:
            print(f"\n{RED}Apenas números{RESET}")
        
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        indice = len(linhas) + 1
        
        cadastrado = Aluno(nome, idade, nota, indice)
        lista_alunos.append(cadastrado)    
        
        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            # Mantemos o padrão usando barras normais para facilitar o split na edição
            arquivo.write(f"{indice} | Nome: {nome} | idade: {idade} | nota: {nota}\n")
        
        print(f"\n{GREEN}Cadastrado com sucesso!{RESET}")
        
        SistemaCadastro.menu()    
        print()
        return input("Escolha uma opção: ") 
    
    @staticmethod
    def menu():
        print(f"\n{CYAN}-------------MENU-------------{RESET}\n")
        print(f"{GREEN}1{RESET} - Cadastrar Alunos")
        print(f"{LIGHT_BLUE}2{RESET} - Listar Alunos")
        print(f"{YELLOW}3{RESET} - Editar Alunos")
        print(f"{RED}4{RESET} - Encerrar Programa\n")
        print(f"{CYAN}------------------------------{RESET}")
        
    @staticmethod
    def listar():
        print(f"\n{LIGHT_BLUE}------------CADASTRADOS----------\n{RESET}")      
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("NENHUM ALUO CADASTRADO AINDA.")
        else:
            for linha in linhas:
                print(linha.strip()) 
        
        print(f"\n{LIGHT_BLUE}--------------------------------{RESET}")              
        SistemaCadastro.menu()
        print()
        return input("Escolha uma opção:")   
    
    @staticmethod
    def editar():
        print("\nOpção 3 ")
        print(f"\n{YELLOW}------------Editar----------\n{RESET}")

        mudanca = input("Pesquise o cadastro desejado? ").strip().lower()


        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        encontrados = []
        linhas_originais_correspondentes = [] # Nova lista para rastrear a linha exata do arquivo

        # BUSCA
        for linha in linhas:
            if mudanca in linha:
                print()
                print(linha.strip())
                partes = linha.split("|")
                encontrados.append(partes)
                linhas_originais_correspondentes.append(linha) # Salva a linha bruta para comparar depois

        if len(encontrados) == 0:
            print("\nCadastro não encontrado!")
            print()
            SistemaCadastro.menu()
            return input("Escolha uma opção:")  

        # ESCOLHA DO ÍNDICE
        print(f"\n{YELLOW}------------Escolha o cadastro------------{RESET}\n")
        escolha_mudanca = input("Digite o indice do cadastro desejado: ").strip()

        encontrado = False
        linha_original_escolhida = ""

        while True:
            for i, partes in enumerate(encontrados):
                if escolha_mudanca == partes[0].strip():
                    print("\nVocê escolheu:\n")
                    print(linhas_originais_correspondentes[i].strip())
                    encontrado = True
                    cadastro_selecionado = partes 
                    linha_original_escolhida = linhas_originais_correspondentes[i] # Guardamos o texto exato antigo
                    break

            if encontrado:
                break

            print("\nÍndice/Dado não encontrado")
            escolha_mudanca = input(f"{RED}Digite novamente o indice do cadastro desejado: {RESET}").strip()
            
        print(f"\n{YELLOW}----------------------\n{RESET}")
        print("1- nome")
        print("2- idade")
        print("3- Nota")
        print(f"\n{YELLOW}----------------------\n{RESET}")
        
        edicao_informacao = input("Digite o número correspondente (1-3): ").strip()
        while edicao_informacao not in("1","2","3"):
            print(f"\n{RED}Deve ser entre 1-3{RESET}")
            edicao_informacao = input("Digite o número correspondente (1-3): ").strip()
        
        novo_dado = input("\nDigite a nova informação: ").strip()
        

        if edicao_informacao == "1":
            cadastro_selecionado[1] = f" Nome: {novo_dado.lower()} "
        elif edicao_informacao == "2":
            cadastro_selecionado[2] = f" idade: {novo_dado} "
        elif edicao_informacao == "3":
            cadastro_selecionado[3] = f" nota: {novo_dado.lower()}\n "

        nova_linha_formatada = "|".join(cadastro_selecionado)
        if not nova_linha_formatada.endswith("\n"):
            nova_linha_formatada += "\n"

        # Substitui a linha antiga BASEADO NA LINHA EXATA ANTERIOR, e não em termos soltos
        for indice, linha in enumerate(linhas):
            if linha == linha_original_escolhida:
                linhas[indice] = nova_linha_formatada
                break

        # Grava de volta no arquivo apagando o antigo ("w")
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)

        print(f"\n{GREEN}Alteração salva com sucesso no arquivo!{RESET}")
        print(f"\n{YELLOW}-----------------------------\n{RESET}")
        SistemaCadastro.menu()
        print()
        return input("Escolha uma opção:")


# --- FLUXO DO PROGRAMA ---
SistemaCadastro.menu()
escolha_opcao = (input("Escolha uma opção: ").strip())
while escolha_opcao not in ("1", "2", "3","4"):
    print("\nDigite entre (1, 2, 3, 4)")    
    escolha_opcao = input("Escolha uma opção: ").strip()

while True: 
    if escolha_opcao == ("1"): 
        print("\nOpção: 1\n")
        escolha_opcao = SistemaCadastro.cadastro(lista_alunos)
        while escolha_opcao not in("1", "2", "3","4"):
            print("\nDigite entre (1, 2, 3, 4)")    
            escolha_opcao = input("Escolha uma opção: ").strip()
    
    if escolha_opcao == ("2"):
        escolha_opcao = SistemaCadastro.listar()
        while escolha_opcao not in("1", "2", "3", "4"):
            print("\nDigite entre (1, 2, 3, 4)")    
            escolha_opcao = input("Escolha uma opção: ").strip()
    
    if escolha_opcao == ("3"):
        escolha_opcao = SistemaCadastro.editar()
        while escolha_opcao not in("1", "2", "3", "4"):
            print("\nDigite entre (1, 2, 3, 4)")    
            escolha_opcao = input("Escolha uma opção: ").strip()
    
    if escolha_opcao == ("4"):
        print(f"{RED}Programa encerrado{RESET}")
        break