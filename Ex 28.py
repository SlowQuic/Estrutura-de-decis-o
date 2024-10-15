def file_duplo(kg):
    if kg <= 5:
        preco = 4.90
    else:
        preco = 5.80
    valor_a_pagar = kg * preco
    if tipo_de_pagamento == "S" or tipo_de_pagamento == "s":
        valor_final = valor_a_pagar - valor_a_pagar * 0.10
    return valor_a_pagar, valor_final

def alcatra(kg):
    if kg <= 5:
        preco = 5.90
    else:
        preco = 6.80
    valor_a_pagar = kg * preco 
    if tipo_de_pagamento == "S" or tipo_de_pagamento == "s":
        valor_final = valor_a_pagar - valor_a_pagar * 0.10
    return valor_a_pagar, valor_final

def picanha(kg):
    if kg <= 5:
        preco = 6.90
    else:
        preco = 7.80
    valor_a_pagar = kg * preco 
    if tipo_de_pagamento == "S" or tipo_de_pagamento == "s":
        valor_final = valor_a_pagar - valor_a_pagar * 0.10
    return valor_a_pagar, valor_final

tipo = input("Digite o tipo de carne: ")
print("-" * 40)
kg = int(input("Quanto kg deseja: "))
print("-" * 40)
tipo_de_pagamento = input("Você deseja fazer a compra no cartão Tabajara (S/N): ")
print("-" * 40)

if tipo == "File duplo" or tipo == "file duplo":
    valor_a_pagar, valor_final = file_duplo(kg)
    print("RECIBO: ")
    print("-" * 40)
elif tipo == "Alcatra" or tipo == "alcatra":
    valor_a_pagar, valor_final = alcatra(kg)
    print("RECIBO: ")
    print("-" * 40)
elif tipo == "Picanha" or tipo == "picanha":
    valor_a_pagar, valor_final = picanha(kg)
    print("RECIBO: ")
    print("-" * 40)

print(tipo.upper())
print("-" * 40)
print(f"Kg: {kg:.0f}")
print("-" * 40)
print(f"Preço total: R${valor_a_pagar:.2f}")
print("-" * 40)
if tipo_de_pagamento == "S" or tipo_de_pagamento == "s":
    print("Tipo de pagamento: Cartão Tabajara")
elif tipo_de_pagamento == "N" or tipo_de_pagamento == "n":
    print("Tipo de pagamento: Alternativo")
print(f"Valor do desconto: R${valor_a_pagar * 0.10}")
print("-" * 40)
print(valor_final)
print("-" * 40)



"""Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""