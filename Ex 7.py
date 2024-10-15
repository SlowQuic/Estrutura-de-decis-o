num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = 0
menor = 0

if num1 > maior:
    maior = num1
    menor = num1
if num2 > maior:
    maior = num2
elif num2 < menor:
    menor = num2
if num3 > maior:
    maior = num3
elif num3 < menor:
    menor = num3
print()

print(f"{maior} é o maior")
print(f"{menor} é o menor")