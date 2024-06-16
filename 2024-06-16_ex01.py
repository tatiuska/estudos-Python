# Exercício 1: Função de Soma
# Crie uma função chamada soma que receba dois números como parâmetros e retorne a soma deles.
# Em seguida, chame a função e exiba o resultado.

# variáveis para receber os números da soma e o resultado
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado: int = 0


# Função Soma
def soma():
    resultado = numero1 + numero2
    return resultado

# Imprimindo e chamando a função soma
print(f"O resultado da soma é: {soma()}")
