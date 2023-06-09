#Exercício 02:
#Crie um dicionário chamado "estoque" com as seguintes chaves e valores
#"Camisetas" - 10, "calças" - 5, "sapatos" - 2
#utilizando um loop for, imprima cada chave e valor do dicionário em linhas separadas

estoque = {"Camisetas": 10, "Calças": 5, "Sapatos": 2}
for item, quantidade in estoque.items():
    print(f"{item} - {quantidade}")