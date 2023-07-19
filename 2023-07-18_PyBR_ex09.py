# Exercício 09: Crie uma função que retorne o reverso de um número inteiro informado
n = int(input("Informe um número inteiro: "))

def inverteNumero(n):
    string = str(n)
    contrario = string[::-1]
    return contrario

print(f"O número digitado {n} invertido é: ", inverteNumero(n))