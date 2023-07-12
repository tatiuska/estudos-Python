# Faça um programa para imprimir:
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def imprimir(numero):
    y = 1
    while y <= numero:
        x = 1
        while x <= y:
            print(x, end="")
            x += 1
        print("")
        y += 1

imprimir(5)