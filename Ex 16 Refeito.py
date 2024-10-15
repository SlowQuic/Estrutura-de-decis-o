import math

def equacao_de_segundo_grau(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("-" * 23)
        print("PROGRAMA ENCERRADO")
    else:
        if delta == 0:
            x = -b / (2 * a)
            print(f"Possui apenas uma raiz, que é: {x:.0f}")
            print("-" * 23)
            print("PROGRAMA ENCERRADO")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"Essa equação tem duas raizes reais, sendo elas:")
            print(f"X1: {x1:.0f}")
            print(f"X2: {x2:.0f}")
            print("-" * 50)
            print()
            print("PROGRAMA ENCERRADO")
            print()

a = float(input("Digite o valor de A: "))
print("-" * 26)
if a != 0:
    b = float(input("Digite o valor de B: "))
    print("-" * 26)
    c = float(input("Digite o valor de C: "))
    print("-" * 50)
    equacao_de_segundo_grau(a, b, c)
else:
    print("O coeficiente A não pode ser 0")
    print("-" * 23)