# Exercício 1: Contagem de Caracteres
# Escreva um programa que conte a frequência de cada caractere em uma string fornecida pelo usuário e exiba o resultado em um dicionário.

dicionario = {}

def conta_caracteres():
    palavra = input("Digite uma palavra: ")
    for i in palavra:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    
    return print(dicionario)


conta_caracteres()