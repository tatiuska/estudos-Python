# Dado um número inteiro digitado pelo usuário, imprima a tabuada desse número até o valor 10.
numero = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    print(f"{numero} * {i} = {i * numero}")