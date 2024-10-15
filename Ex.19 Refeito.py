def resultado(x):
    seculos = num // 100
    resto_seculos = num % 100
    dezenas = resto_seculos // 10
    resto_dezenas = resto_seculos % 10
    unidade = resto_dezenas // 1
    final = (f"{seculos}/{dezenas}/{unidade}")
    return final

while True:
    num = int(input("Digite um numero: "))
    if num <= 1000:
        break
    else:
        print("-" * 40)
        print("Digite um numero menor ou igual a 1000")
        print("-" * 40)
    
print("-" * 20)
print(resultado(num))