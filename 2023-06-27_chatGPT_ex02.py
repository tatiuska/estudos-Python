# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = float(input("Informe o preço do primeiro produto: "))
p2 = float(input("Informe o preço do segundo produto: "))
p3 = float(input("Informe o preço do terceiro produto: "))

if p1 < p2 and p1 < p3:
    print(f"O produto a ser comprado é o produto que custa R$ {p1}")
if p2 < p3 and p2 < p1:
    print(f"O produto a ser comprado é o produto que custa R$ {p2}")
if p3 < p1 and p3 < p2:
    print(f"O produto a ser comprado é o produto que custa R$ {p3}")