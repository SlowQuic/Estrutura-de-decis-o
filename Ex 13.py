dia_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

x = int(input("Digite um número: "))

if x <= 31:
    while True:
        if x > 7:
            x = x -7
        else:
            break
    print(dia_semana[x - 1])
else:
    print("VALOR INVÁLIDO")
    