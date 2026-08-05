# PDF de Programação e algoritmo completo resumo

# lógica de Programação: forma correta de pensar e organizar passos, 4Passos: Ordem, Clareza, Sequencia de ações e Objetivo bem definido

# Alogoritmo: sequencia lógica e ordenada de passos, ordem de resolver problemas

#Codigo-Fonte: código escrito pelo programador de uma forma legível para pessoas
#Código Objeto: linguagem próxima a linguagem da máquina
#Executável: programa pronto para ser executado

#Compiladores: traduz o programa de uma vez, gera um arquivo executável, ex:C, C++
#Interpretadores: executa linha por linha, não gera arquivo final, ex:py

#Kits de desenvolvemento(SDK): conjunto de ferrametas utilizadas para desenvolver software
#Ambiente de desenvolvimento integrado(IDEs): programas que facilitam a escrita, execução e organizaçaõ do código, ex:VScode
#Bibliotecas: conjunto de códigos prontos que podem ser reutilizados, ex em py:math, tkinter
#Frameworks: estruturas mais completas que organizam o desenvolvimento de aplicações

#Variaveis: é um espaço na memória do computador utilizado para armazenar valores temporários durante a execução do programa, criada apartir que recebe um valor
#int: inteiro(numeros), float: real(numeros com casas decimais), str: texto(""), bool: booleano(valores logicos)
#imput:permite que o usuario informe dados pelo teclado(recebe dados do usuario)

#Expressões Aritméticas: +(adição), -(Subtraçao), *(multiplicaçao), /(Divisão), //(divisao inteira), %(Resto da divisao), **(potencia)
#Expressões relacionais: ==(Atribuicao), !=(diferente de), >(maior que), <(menor que), >=(maior ou igual), <=(menor ou igual)
#Expressões logicas: and,or,not

#LAÇO WHILE: executa um bloco de código enquanto a condiçao for verdadeira, ex: contador =1 while contador <=5:print(contador) contador +=1
#LAÇO FOR: Utilizados quando se sabe quantas vezes o bloco deve repetir: for i in range(inicio, fim)

#FUNÇÕES: def nome():comando

#ESTRUTURAS DE DADOS COMPOSTOS
    # LISTAS(list): armazena valores em uma unica variavel e são mutaveis, ex: nume = [10, 20, 30, 40] alterando: nume[1] = 25
    #percorendo a lista com for ex: for n in nume: print(n)
    # TUPLAS(tuple): são imutaveis, ex: cor = ("VERMELHO", "AZUL", "VERDE") print(cor[1]), utiliza tuplas quando os valores não podem ser modificados
    # DICIONARIOS: armazenam valores no formato chave:valor ex: aluno = {"nome": "joão"}
    #percorrendo dicionario com for ex: for chave in aluno: print(chave, ":", aluno[chave])

#Tratamentos de erro:try e except ex:
    #try numero = int(input("Digite un numero")) print("Numero digitado:", numero)
    #except: print("Valor inválido") ESTUDAR MAIS

#MANIPULAÇÃO DE DADOS E SAIDA
   #FUNÇÃO len(): retorna quantidade de elementos da estrutura de dados 
    #MÉTODO .append(""): adiciona elementos ao final de uma lista(armazenar dados informados pelo usuário)
    # .lower():(converte texto para minúsculo)
    # .upper(): (converte texto para maiúsculo)
    # f-strings(formatação de texto): permite variáveis diretamente dos textos, ex: nome = "Maria" print(f"Aluno: {nome})
    # DICIONARIOS E ACESSO POR CHAVES, ex: aluno = {"nome": "Ana", "nota": 8} print(aluno["nome"])
        #uso com f-string: print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota']}")   
    #MÉTODO .replace("valor_antigo", "valor_novo")
    # MÉTODO .strip(): remove espaços no ini´cio e no fim
    # MÉTODO .split(): divide o texto em partes(lista), ex: tex = "py java C" linguagem = tex.split() print(linguagem) saida: ['py', 'java','C']
    # MÉTODO .join(): junta elementos em uma lista em uma string 
    # Operador in: verifica se algo existe, ex: nome = "Enildo" print("E" in nome)  true
    # none: sem valor, ex: valor = none  if valor is none: print("Sem valor")

#POO: PROGRAMAÇÃO ORIENTADA A OBJETO
    #programação baseada na organização do codigo em objetos, que representam entidades do mundo real
    # cada objeto possui: atributos(características), métodos(comportamentos)
#Classe e objeto
    #classe: é um modelo(estrutura) que define um tipo de objeto, é a parte superficial das coisas, como se fosse um documento original mas sem expecificação
    #objeto: é uma instáncia de uma classe, ex: classe atributos: marca, cor, ano, modelo Métodos(funções dentro da classe):ligar,acelerar,frear,buzinar ; ele é o documentario com mais modelo, especificação, caracteristicas coisas novas
    #__init__: método construtor da classe
    #self: referencia ao próprio objeto
#HERANÇA: permite uma classe herde caractéristicas de outra, evite repetição de código e facilita manutenção
#POLIMORFISMO: múltiplas formas,o mesmo método tem comportamentos diferentes
#ENCAPSULAMENTO: Proteger os dados internos de uma classe, controlando a forma como eles podem ser acessados ou modificados, atributos proteger

#get(getters): obter valor e set(setters):alterar valor; são métodos usados para controlar o acesso aos atributos privados