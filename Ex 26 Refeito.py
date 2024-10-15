def gasolina(quan_litros):
    preco = 2.50
    if quan_litros <= 20:
        desconto = quan_litros * (preco * 0.04)
    else:
        desconto = quan_litros * (preco * 0.06)
    valor_a_pagar = quan_litros * preco - desconto
    return valor_a_pagar
def alcool(quan_litros):
    preco = 1.90
    if quan_litros <= 20:
        desconto = quan_litros * (preco * 0.03)
    else:
        desconto = quan_litros * (preco * 0.05)
    valor_a_pagar = (quan_litros * preco) - desconto
    return valor_a_pagar

quan_litros = int(input("Digite quantos litros você deseja: "))
print("-" * 50)
tipo = input("Digite o tipo do combustivel (G/A): ")
print("-" * 50)

if tipo == "G" or tipo == "g":
    print(f"Valor a pagar: {gasolina(quan_litros):.2f}")
    print("-" * 50)
elif tipo == "A" or tipo == "a":
    print(f"Valor a pagar: {alcool(quan_litros):.2f}")
    print("-" * 50)
else:
    print("INVALIDO, DIGITE UMA DAS OPÇÕES")
    print("-" * 50)