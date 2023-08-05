# Exercício 14: Um quadrado mágico é aquele dividido em linhas e colunas,
# com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

# Função para definir se um quadrado é mágico. Para tal, a soma de todas as linhas, colunas e diagonais deverá ser 15.
def magico(l):
    l1 = sum([l[0], l[1], l[2]])
    l2 = sum([l[3], l[4], l[5]])
    l3 = sum([l[6], l[7], l[8]])

    c1 = sum([l[0], l[3], l[6]])
    c2 = sum([l[1], l[4], l[7]])
    c3 = sum([l[2], l[5], l[8]])

    d1 = sum([l[0], l[4], l[8]])
    d2 = sum([l[2], l[4], l[6]])

    return l1 == l2 == l3 and c1 == c2 == c3 and d1 == d2


# Função para testar os números de uma lista usando o laço de repetição for
# (não é a resolução que corresponde à melhor prática)
def checklist():
    for i1 in range(1, 10):
        for i2 in range(1, 10):
            for i3 in range(1, 10):
                for i4 in range(1, 10):
                    for i5 in range(1, 10):
                        for i6 in range(1, 10):
                            for i7 in range(1, 10):
                                for i8 in range(1, 10):
                                    for i9 in range(1, 10):
                                        lista = [i1, i2, i3,
                                                 i4, i5, i6,
                                                 i7, i8, i9]
                                        if magico(lista):
                                            print(lista)


# Chamando a função lista
checklist()
