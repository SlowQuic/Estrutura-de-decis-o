dia = {"M", "m"}
tarde = {"V", "v"}
noite = {"N", "n"}

print("M-matutino ou V-Vespertino ou N- Noturno")
x = input("Digite o turno em que você estuda: ")

if x.lower() in dia:
    print("Bom dia")
elif x.lower() in tarde:
    print("Boa tarde")
elif x.lower() in noite:
    print("Boa noite")
else:
    print("Inválido")