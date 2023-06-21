# Dada uma lista de números, calcule e imprima a média dos elementos utilizando um loop for.
numeros = [11, 56, 189, 21, 8, 13, 7]
total = 0
for i in numeros:
    total += i
media = total / len(numeros)
print(media)