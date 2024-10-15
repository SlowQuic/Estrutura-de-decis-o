def calcular_preco(tipo_carne, quantidade, tipo_pagamento="N"):
    if tipo_carne.lower() == "file duplo":
        preco_base = 4.90 if quantidade <= 5 else 5.80
    elif tipo_carne.lower() == "alcatra":
        preco_base = 5.90 if quantidade <= 5 else 6.80
    elif tipo_carne.lower() == "picanha":
        preco_base = 6.90 if quantidade <= 5 else 7.80
    else:
        return "Tipo de carne inválido."

    valor_total = quantidade * preco_base
    if tipo_pagamento.lower() == "s":
        valor_total *= 0.9  # Desconto de 10%
    return valor_total

# Entrada do usuário
tipo_carne = input("Digite o tipo de carne: ")
quantidade = float(input("Quanto kg deseja: "))
tipo_pagamento = input("Você deseja fazer a compra no cartão Tabajara (S/N): ")

# Cálculo e exibição do recibo
valor_total = calcular_preco(tipo_carne, quantidade, tipo_pagamento)

if isinstance(valor_total, str):
    print(valor_total)
else:
    desconto = valor_total * 0.1 if tipo_pagamento.lower() == "s" else 0
    print("RECIBO:")
    print("-" * 40)
    print(f"Tipo de carne: {tipo_carne.upper()}")
    print(f"Quantidade: {quantidade:.2f} kg")
    print(f"Preço total: R${valor_total:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${valor_total - desconto:.2f}")
    print("-" * 40)