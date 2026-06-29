try:
    valor = float(input("Digite o valor: "))
    quantidade = int(input("Digite a quantidade: "))
    print("Total: ", valor * quantidade)
except:
    print("Erro ao calcular.")