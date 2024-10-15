lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))
media = (lado1 + lado2 + lado3) // 3

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")