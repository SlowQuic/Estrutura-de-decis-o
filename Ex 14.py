nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 0 and media <= 4:
    print("NOTA: E")
elif media < 6:
    print("NOTA: D")
elif media < 7.5:
    print("NOTA: C")
elif media < 9:
    print("NOTA: B")
elif media <= 10:
    print("NOTA: A")