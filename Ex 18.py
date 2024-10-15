dia = int(input("Digite o dia: "))

if dia > 0 and dia <= 31:
    mes = int(input("Digite o mês: "))
    if mes > 0 and mes <= 12:
        ano = int(input("Digite o ano: "))
    else:
        print("Mês Inválido")
else:
    print("Dia Inválido")

print(f"Data: {dia}/{mes}/{ano}")