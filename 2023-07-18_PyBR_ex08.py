# Fazer uma função que informe a quantidade de dígitos de um determinado número inteiro informado:
def qtdDigitos(n):
    return len(str(n))
def mostraDigitos():
    n = int(input("informe um número inteiro: "))
    print(f"O número informado possui ", qtdDigitos(n), " dígitos")

while True:
    mostraDigitos()