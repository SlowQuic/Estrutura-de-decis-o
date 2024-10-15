import math
a = float(input("Digite o valor de A: "))

if a != 0:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    if delta < 0:
        print("PROGRAMA ENCERRADO")
    else:
        if delta == 0:
            print(f"Essa equação tem apenas uma raiz real, que é a {x1:.0}")
        else:
            print(f"Essa equação tem duas raizes reais, sendo elas:")
            print(x1)
            print(x2)
else:
    print("PROGRAMA ENCERRADO")