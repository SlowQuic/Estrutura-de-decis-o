vogais = {"a", "e", "i", "o", "u"}
x = input("Digite uma letra: ")

if x.lower() in vogais:
    print("Vogal")
else:
    print("Consoante")