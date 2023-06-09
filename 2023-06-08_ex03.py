#Exercício 03:
#Crie um dicionário chamado "precos" com as seguintes chaves e valores: "maçã" - 2.5, "banana" - 1.8, "laranja" - 3.1. Utilizando um loop for, calcule e imprima o preço total de todos os itens.
precos = {"Maçã": 2.5, "Banana": 1.8, "Laranja": 3.1}
total = 0
for item in precos.values():
    total = total + item
print(total)