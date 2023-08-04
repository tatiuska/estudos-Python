# Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista vistos no Capítulo 7
# Programa 8.1
# def pesquise(lista, valor):
#     for x, e in enumerate(lista):
#         if e == valor:
#             return x
#     return None

def pesquisar(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

l = [10, 20, 30, 40, 50]

print(pesquisar(l, 100))