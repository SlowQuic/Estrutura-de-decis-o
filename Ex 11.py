def reajuste(x):
    if x <= 280:
        percentual = 0.2
    elif x <= 700:
        percentual = 0.15
    elif x <= 1500:
        percentual = 0.1
    elif x > 1500:
        percentual = 0.05
    
    aumento = salario_antigo * percentual
    salario_novo = salario_antigo + aumento
    return percentual, aumento, salario_novo

salario_antigo = float(input("Digite seu salário atual: "))
percentual, aumento, salario_novo = reajuste(salario_antigo)

print()
print(f"Salário pré-reajuste: {salario_antigo}")
print(f"Aumento de: {percentual*100:.2f}%")
print(f"Valor do aumento: {aumento}")
print(f"Salário após reajuste: {salario_novo}")