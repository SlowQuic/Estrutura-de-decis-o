def imposto(x):
    if x <= 900:
        percentual = 0
    elif x <= 1500:
        percentual = 0.05
    elif x <= 2500:
        percentual = 0.1
    
    IR = salario_bruto * percentual
    INSS = salario_bruto * 0.1
    FGTS = salario_bruto * 0.11
    total_descontos = IR + INSS
    salario_liquido = salario_bruto - total_descontos
    return percentual, IR, INSS, FGTS, total_descontos, salario_liquido

valor_hora = float(input("Digite o valor da sua hora: "))
quan_hora = int(input("Digite quantas horas você trabalhou: "))
salario_bruto = valor_hora * quan_hora
percentual, IR, INSS, FGTS, total_descontos, salario_liquido = imposto(salario_bruto)

print()
print(f"Salário Bruto: ({quan_hora} * {valor_hora:.0f}) {"":>10}: R$ {salario_bruto:.2f}")
print(f"IR ({percentual*100:.0f}%) {"":>27}: R$ {IR:.2f}")
print(f"INSS (10%) {"":>24}: R$ {INSS:.2f}")
print(f"FGTS (11%) {"":>24}: R$ {FGTS:.2f}")
print(f"Total de descontos {"":>16}: R$ {total_descontos:.2f}")
print(f"Salário Liquido {"":>19}: R$ {salario_liquido:.2f}")