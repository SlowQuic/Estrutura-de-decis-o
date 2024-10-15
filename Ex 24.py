def par_ou_impar(x1, x2):
    if (x1 % 2) == 0:
        resposta1 = "Número Par"
    else:
        resposta1 = "Número Ímpar"
    if (x2 % 2) == 0:
        resposta2 = "Número Par"
    else:
        resposta2 = "Número Ímpar"
    return resposta1, resposta2

def inteiro_ou_decimal(x1, x2):
    x1 = x1 % 1
    if x1 != 0:
        resposta1 = "Número Decimal"
    else:
        resposta1 = "Número Inteiro"
    x2 = x2 % 1
    if x2 != 0:
        resposta2 = "Número Decimal"
    else:
        resposta2 = "Número Inteiro"
    return resposta1, resposta2

def positivo_ou_negativo(x1, x2):
    if x1 > 0:
        resposta1 = "Positivo"
    elif x1 < 0:
        resposta1 = "Negativo"
    if x2 > 0:
        resposta2 = "Positivo"
    elif x2 < 0:
        resposta2 = "Negativo"
    return resposta1, resposta2

print("-" * 20)
num1 = float(input("Digite o valor do número 1: "))
num2 = float(input("Digite o valor do número 2: "))
print("-" * 20)

print("Qual operação você deseja fazer: ")
print("a. par ou ímpar")
print("b. positivo ou negativo")
print("c. inteiro ou decimal")
decisao = input("Opção: ")
print("-" * 20)

if decisao == "a":
    resposta1, resposta2 = par_ou_impar(num1, num2)
    print(f"{resposta1}/{resposta2}")
    print("-" * 20)
elif decisao == "b":
    resposta1, resposta2 = positivo_ou_negativo(num1, num2)
    print(f"{resposta1}/{resposta2}")
    print("-" * 20)
elif decisao == "c":
    resposta1, resposta2 = inteiro_ou_decimal(num1, num2)
    print(f"{resposta1}/{resposta2}")
    print("-" * 20)
else:
    print("INVÁLIDO")