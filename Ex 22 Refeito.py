def par_ou_impar(x):
    if (x % 2) != 0:
        resposta = "Número Ímpar"
    else:
        resposta = "Número Par"
    return resposta

print("-" * 20)
num = int(input("Digite um número: "))
print("-" * 20)
print(par_ou_impar(num))
print("-" * 20)