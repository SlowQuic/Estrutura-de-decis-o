mas = {"M", "m"}
fem = {"F", "f"}
gen = input("Digite seu gênero: ")

if gen.lower() in mas:
    print("Masculino")
elif gen.lower() in fem:
    print("Feminino")
else:
    print("SEXO INVÁLIDO")
