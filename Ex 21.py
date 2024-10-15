valor = int(input("Digite o valor a sacar: R$"))

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

print(f"{n100}/{n50}/{n10}/{n5}/{n1}")