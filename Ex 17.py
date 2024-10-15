ano = int(input("Digite um ano: "))
resto = ano % 4

if resto == 0:
    print("Ano Bissexto")
else:
    print("Não é um Ano Bissexto")
