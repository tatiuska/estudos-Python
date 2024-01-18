# Funções
from random import randint
def rola_dados(dados, faces):
    #resultado = []

    #Op 1: While
    #i = 0
    #while i < dados:
    #    resultado.append(randint(1, faces))
    #    i += 1

    #Op 2: For
    #for i in range(dados):
    #    resultado.append(randint(1, faces))
    #    i += 1

    #Op 3: List Comprehension
    resultado = [randint(1, faces) for _ in range(dados)]
    # resultado = [randint(i, faces) for i in range(dados)]

    return resultado

entrada = ""

while entrada != "X":
    entrada = input("Aperte D para rolar os dados ou X para sair. ").upper()
    if entrada == "D":
        vezes = int(input("Digite o número de vezes para rolar os dados: "))
        faces = int(input("Digite o número de faces dos dados: "))
        resultado = rola_dados(vezes, faces)
        print(f"o resultado de {vezes} é {resultado}.")
