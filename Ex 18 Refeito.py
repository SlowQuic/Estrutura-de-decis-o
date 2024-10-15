def montando_data(x, y, z):
    data = (f"{x}/{y}/{z}")
    return data

dia = int(input("Digite o dia: "))
print("-" * 23)

if dia > 0 and dia <= 28:
    mes = int(input("Digite o mês: "))
    print("-" * 23)
    if mes > 0 and mes <= 12:
        ano = int(input("Digite o ano: "))
        print("-" * 23)
        if ano > 0 and ano < 10000:
            print(f"Data: {montando_data(dia, mes, ano)}")
        else:
            print("POR FAVOR, COLOQUE UM ANO ENTRE 1 e 9999")
    else:
        print("Mês Inválido")
elif dia <= 31:
    mes = int(input("Digite o mês: "))
    print("-" * 23)
    if mes != 2:
        ano = int(input("Digite o ano: "))
        print("-" * 23)
        if ano > 0 and ano < 10000:
            print(f"Data: {montando_data(dia, mes, ano)}")
        else:
            print("POR FAVOR, COLOQUE UM ANO ENTRE 1 e 9999")
    else:
        print("DATA INVALIDA")