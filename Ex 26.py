quan_litros = int(input("Digite quantos litros você deseja: "))
tipo = input("Digite o tipo de combustível (A ou G): ")

if tipo == "a" or tipo == "A":
    preco = 2.50
    if quan_litros <= 20:
        desconto = quan_litros * (preco * 0.03)
    else:
        desconto = quan_litros * (preco * 0.05)
    valor_a_pagar = quan_litros * preco - desconto
elif tipo == "g" or tipo == "G":
    preco = 1.90
    if quan_litros <= 20:
        desconto = quan_litros * (preco * 0.04)
    else:
        desconto = quan_litros * (preco * 0.06)
    valor_a_pagar = quan_litros * preco - desconto

print(f"Valor a pagar: {valor_a_pagar:.2f}")