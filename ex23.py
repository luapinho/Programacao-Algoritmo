try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Soma: ", n1 + n2)

except ValueError:
    print("Erro nos dados. Digite apenas números.")