# Exercício 3: Função de Verificação de Paridade
# Escreva uma função chamada eh_par que receba um número como parâmetro e retorne True se o número for par,
# e False caso contrário.


# Função para saber se o número é par
def eh_par():
    # Variável vai receber o input, tipado em int
    numero = int(input("Digite um número: "))

    # Aplicação da etsrutura condicional if/else
    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é ímpar!")


# Chamando a função
eh_par()


# # versão 2
# def eh_par(x: int) -> bool:
#     if x % 2:
#         return False
#     else:
#         return True
#
# print(eh_par(44))
