def quantidade_de_notas(x):
    n100 = valor // 100
    resto = valor % 100
    n50 = resto // 50
    resto = resto % 50
    n10 = resto // 10
    resto = resto % 10
    n5 = resto // 5
    resto = resto % 5
    n1 = resto // 1
    resto = resto % 1
    return (f"Notas de 100: {n100} - Notas de 50: {n50} - Notas de 10: {n10} - Notas de 5: {n5} - Notas de 1: {n1}")

valor = int(input("Digite o valor: R$"))
print("-" * 85)
print(quantidade_de_notas(valor))
print("-" * 85)