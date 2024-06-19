# Exercício 02: Função de Fatorial
# Escreva uma função chamada fatorial que receba um número como parâmetro e retorne o fatorial desse número

# Variáveis
numero = int(input("Insira um número: "))


# Função fatorial
def fatorial(numero) -> int:
    if numero == 0 or numero == 1:
        return 1
    else:
        calculo = numero * fatorial(numero - 1)
        return calculo


# Imprimindo o resultado
print(f"O fatorial de {numero}! é: {fatorial(numero)}")
