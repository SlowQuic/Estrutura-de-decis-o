num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print()
if num1 > num2 and num3:
    print("O primeiro número é o maior")
elif num2 > num3:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")