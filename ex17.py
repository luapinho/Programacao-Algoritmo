def maior_de_idade(idade):
    if idade >=18:
        return "maior de idade"
    else:
        return "menor de idade"

idade = int(input("Digite a sua idade: "))
resultado = maior_de_idade(idade)
print("Resultado: ", resultado)