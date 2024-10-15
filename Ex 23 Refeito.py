def inteiro_ou_decimal(x):
    x = x % 1
    if x != 0:
        resposta = "Número Decimal"
    else:
        resposta = "Número Inteiro"
    return resposta

print("-" * 20)
num = float(input("Digite um número: "))
print("-" * 20)
print(inteiro_ou_decimal(num))
print("-" * 20)