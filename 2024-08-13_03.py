# Exercício 5: Alternando Caracteres
# Solicite ao usuário que insira uma frase e exiba apenas os caracteres que estão em posições ímpares da string.

def alterna_caracteres():
    frase = input("Digite uma frase: ")
    return print(frase[1::2])


alterna_caracteres()