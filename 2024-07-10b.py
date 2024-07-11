# algoritmo para converter inteiros para algarismos romanos, última versão do artigo do medium. originalmente escrito
# em JS.

from math import floor


def to_roman8(num):
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']

    return thousands[floor(num / 1000)] + hundreds[floor((num % 1000) / 100)] + tens[floor((num % 100) / 10)] + \
        ones[num % 10]


numero = 1989
print(to_roman8(numero))