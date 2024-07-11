# algoritmo de artigo no medium para conversão de números inteiros para algarismos romanos, originalmente escrito em JS.
# foi um dos primeiros da lista, incompleto.

def to_roman(num):
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    result = ''
    radix = 5
    while num:
        result = letters.pop(0) * (num % radix) + result
        num //= radix
        radix ^= 7
    return result


print(to_roman(2734))