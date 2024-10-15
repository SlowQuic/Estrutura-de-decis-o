def resto(ano):
    resto = ano % 4
    return resto

ano = int(input("Digite um ano: "))

if resto(ano) == 0:
    print("Ano Bissexto")
else:
    print("Não é um Ano Bissexto")