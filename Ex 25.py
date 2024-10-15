def veredito(suspeitagem):
    if suspeitagem == 5:
        resposta = "ASSASSINO"
    elif suspeitagem >= 3:
        resposta = "CÚMPLICE"
    elif suspeitagem == 2:
        resposta = "SUSPEITO"
    else:
        resposta = "INOCENTE"
    return resposta

positivo = {"S", "s"}
suspeitagem = 0

Q1 = input("Telefonou para a vítima? S/N: ")
Q1 = Q1.lower()
print("-" * 40)
if Q1 in positivo:
    suspeitagem += 1 
Q2 = input("Esteve no local do crime? S/N: ")
Q2 = Q2.lower()
print("-" * 40)
if Q2 in positivo:
    suspeitagem += 1  
Q3 = input("Mora perto da vítima? S/N: ")
Q3 = Q3.lower()
print("-" * 40)
if Q3 in positivo:
    suspeitagem += 1 
Q4 = input("Devia para a vítima? S/N: ")
Q4 = Q4.lower()
print("-" * 40)
if Q4 in positivo:
    suspeitagem += 1 
Q5 = input("Já trabalhou com a vítima? S/N: ")
Q5 = Q5.lower()
print("-" * 40)
if Q5 in positivo:
    suspeitagem += 1 

print(f"Veredito: {veredito(suspeitagem)}")
print("-" * 40)