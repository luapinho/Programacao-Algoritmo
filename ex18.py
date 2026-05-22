def conta(valor,quantidade):
    return valor * quantidade

valor = float(input("Digite o seu valor: "))
quantidade = int(input("Digite a quantidade: "))
resultado = conta(valor,quantidade)
print("Resultado", resultado)