print("\nComparando números")
num1 = int(input("\nDigite um número:"))
num2 = int(input("Digite um segundo número:"))
num3 = int(input("Digite um terceiro número:"))

if num1 <= num2 and num1 <= num3:
    print("Número menor: " , num1)

elif num2 <= num1 and num2 <= num3:
    print("Número menor: ", num2)

else:
    print("Número menor: ", num3)