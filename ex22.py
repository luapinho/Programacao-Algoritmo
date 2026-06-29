try:
    numero = int(input("Digite um número: "))
    print("Número: ", numero)

except ValueError:
    print("Entrada inválida. Digite apenas números.")