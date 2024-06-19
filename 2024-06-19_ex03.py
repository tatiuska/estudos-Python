# Exercício 3: Função de Verificação de Paridade
# Escreva uma função chamada eh_par que receba um número como parâmetro e retorne True se o número for par,
# e False caso contrário.


def eh_par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é ímpar!")


eh_par()
