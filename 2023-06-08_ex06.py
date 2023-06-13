# Exercício 6:
# Crie um dicionário chamado "estoque" com as seguintes chaves e valores: "camisetas" - 20, "calças" - 15,
# "sapatos" - 10. Usando um 'loop' for, verifique se algum item do estoque possui uma quantidade menor que 10.
# Se houver, imprima o nome do item.

estoque = {"camisetas": 20, "calcas": 15, "sapatos": 10}
for item, qtd in estoque.items():
    if qtd <= 10:
        print(f"{item}");