produtos = {
    "Produto 1": float(input("Digite o preço do produto 1 = ")),
    "Produto 2": float(input("Digite o preço do produto 2 = ")),
    "Produto 3": float(input("Digite o preço do produto 3 = "))
}

menor_preco = min(produtos.values())
for produto, preco in produtos.items():
    if preco == menor_preco:
        print(f"O produto com o menor preço é {produto}")