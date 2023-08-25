# A sequência de Fibonacci é uma sequência de números em que cada número é a soma dos dois números anteriores.
# A sequência começa com 0 e 1.
# Por exemplo:
# Os primeiros números na sequência de Fibonacci são 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# O desafio é criar uma função recursiva em Python chamada fibonacci que recebe um número inteiro N como parâmetro e
# retorna o N-ésimo número na sequência de Fibonacci.

def fibonacci(n):
    if n == 1 or n == 0:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(11))