num = int(input("Digite um numero: "))

seculos = num // 100
resto_seculos = num % 100
dezenas = resto_seculos // 10
resto_dezenas = resto_seculos % 10
unidade = resto_dezenas // 1

print(f"{seculos}/{dezenas}/{unidade}")
