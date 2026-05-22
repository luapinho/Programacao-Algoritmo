while True:
    nome_do_cliente = input("Digite o seu nome:").capitalize()
    produtos_comprados = int(input("Digite a quantidade de produtos"))

    total = 0
    for i in range(produtos_comprados):
       print(f"\nproduto {i+1}")
       produto = input("Digite o nome do produto:")
       preço = float(input("Digite o preço do produto:"))
       quantidade = int(input("Digite a quantidade de produto:"))

    subtotal = preço * quantidade
    total_da_compra = total + subtotal
    print("subtotal:", subtotal)
    
    if total_da_compra >= 500:
     desconto = total_da_compra * 0.1
    elif total_da_compra >= 200:
       desconto = total_da_compra * 0.05
    else:
       desconto = 0   

    print("---Resultado---")
    total_final = total_da_compra - desconto
    print ("cliente:", nome_do_cliente)
    print ("total da compra:", total_da_compra)
    print ("desconto:", desconto)
    print ("total final:", total_final)

    nova_venda = input("Deseja realizar uma nova compra? se não digite n :").lower()
    if nova_venda == "n" :
       break
    print("Programa encerrado")