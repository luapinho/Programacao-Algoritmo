#funções
def classificação_aluno(nota): # criando uma função para calcular 
    if nota >=7: # uma condição, que vai testar se for vdd ela executa o return
        return "Aprovado"
    elif nota >=5: # uma segunda opção caso o if seja falso 
        return "Recuperação"
    else: # o ultimo teste
        return "Reprovado"
    

def calcular_media(alunos):
    soma = 0 #cria uma varivel soma começando em 0
    
    if len(alunos) == 0:  # verificação antes do cálculo
        return 0

    for aluno in alunos: #percorre cada aluno dentro da lista alunos
        soma = soma + aluno["nota"] #pega a nota de cada aluno e soma na variavel soma
        
    return soma / len(alunos)  #divide a soma pela quantidade de alunos


def maior_nota(alunos):
    maior = alunos[0] #assume que o primeiro aluno é o maior(ponto inicial)
    for aluno in alunos: #percorre todos os alunos
        if aluno["nota"] > maior["nota"]: #compara a nota atual com a maior armazenada
            maior = aluno #se for maior, atualiza o valor de maior
    return maior #retorna o aluno com maior nota


def menor_nota(alunos):
    menor = alunos[0] #assume que o primeiro aluno é o menor
    for aluno in alunos:
        if aluno["nota"] < menor["nota"]: #compara a nota atual com a menor armazenada
            menor = aluno #se for menor atualiza
    return menor
    

alunos = [] # criou uma lista vazia para guardar

while True: #laço de repetição,ele vai executar o codigo enquanto for verdadeiro
    nome = input("Nome do aluno: ")

    while True: # loop para validar a idade
        try: # evita falhas ou erros,tenta executar o código
            idade = int(input("Idade: "))
            if idade > 0: #verifica se a idade é válida
                break #acaba se caso estiver correto
            else: #se a idade for inválida
                print("Idade deve ser maior que 0.") #mostra mensagem de erro
        except: #se der errado(ex: usuario digitar texto)
            print("Digite um número válido.")

    while True: #loop para validar a nota
        try: #tenta executar
            nota = float(input("Nota: ")).replace(".", ",")
            if 0 <= nota <=10: #verifica se esta entre 0 e 10
                break #encerra o loop
            else:
                print("A nota deve ser somente entre 0 e 10.") #erro caso ele não incira entre 0 e 10
        except:
            print("Digite um número válido.") #erro se não for número

    situação = classificação_aluno(nota) #chama a função e guarda o resultado (ex:aprovado)

    aluno = { #dicionario com os dados do aluno
        "nome": nome, #chave nome recebe o valor digitado
        "idade": idade,
        "nota": nota,
        "situação": situação
    }

    alunos.append(aluno) #adiciona tudo da lista no dicionario
    
    while True: #laço infinito,ate chegar nesse break final,pq ele so para se encontrar um break
        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
        
        if continuar == 's' or continuar == 'n': #se o usuario digitar s ou n,ta verificando a resposta
            break
        else:
            print("Digite apenas 's' ou 'n'.") #aqui se ele digitou outra coisa,vai aparecer na tela dele o print

    if continuar == 'n': #se o usuario digitar n ele para o laço principal,ai encerra o cadastro e vai pro relatório
        break

# relatório final
print ("--- RESULTADO ---")
aprovados = 0 #contador de alunos começa em 0
recuperação = 0
reprovados = 0

for aluno in alunos:
    print(f"Aluno: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f} | Situação: {aluno['situação']}")

    if aluno["situação"] == "Aprovado": #verifica se situação é igual a condição
        aprovados = aprovados + 1 # soma 1 ao contador
    elif aluno["situação"] == "Recuperação":
        recuperação = recuperação + 1
    else:
        reprovados = reprovados + 1
        
media = calcular_media(alunos) #chama a função para calcular média da turma

print(f"\nMedia da turma: {media:.2f}") #mostra a média da turma
print("Aprovados: ", aprovados)
print("Recuperação: ", recuperação)
print("Reprovados: ", reprovados)

if alunos: #verifica se a lista não está vazia
    maior = maior_nota(alunos) #função criada
    menor = menor_nota(alunos)

    print(f"\nAluno com maior nota: {maior['nome']} - {maior['nota']:.1f}") #mostra o resultado de desempenho
    print(f"Aluno com menor nota: {menor['nome']} - {menor['nota']:.1f}")