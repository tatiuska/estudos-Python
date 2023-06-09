# Exercício 5:
# Crie um dicionário chamado "palavras" com as seguintes chaves e valores: "python" - 6, "programação" - 12, "linguagem" - 9.
# Utilizando um loop for, imprima apenas as chaves que possuem um número par de caracteres.
palavras = {"python": 6, "programação": 11, "linguagem": 9}
for palavra in palavras:
    if len(palavra) % 2 == 0:
        print(palavra)