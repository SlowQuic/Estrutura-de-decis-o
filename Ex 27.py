def morango(kg):
    if kg <= 5:
        preco = 2.50
    else:
        preco = 2.20
    valor_a_pagar = kg * preco
    if kg >= 8 or valor_a_pagar >= 25:
        valor_a_pagar = valor_a_pagar - (valor_a_pagar * 0.10)
    return valor_a_pagar
    
def maca(kg):
    if kg <= 5:
        preco = 1.80
    else:
        preco = 1.50
    valor_a_pagar = kg * preco
    if kg >= 8 or valor_a_pagar >= 25:
        valor_a_pagar = valor_a_pagar - (valor_a_pagar * 0.10)
    return valor_a_pagar

print("-" * 54)
tipo = input("Digite qual fruta você quer (Morango/Maça): ")
print("-" * 54)
kg = int(input("Digite quantos KG você deseja: "))
print("-" * 54)

if tipo == "Morango" or tipo == "morango":
    print(f"Valor a pagar: R${morango(kg):.2f}")
    print("-" * 54)
elif tipo == "Maça" or tipo == "maça":
    print(f"Valor a pagar: R${maca(kg):.2f}")
    print("-" * 54)
else:
    print("OPÇÃO INESISTENTE")
    print("-" * 54)