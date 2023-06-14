# Exercício 10:
# Crie um dicionário chamado "palavras" com as seguintes chaves e valores: "python" - 6, "programação" - 12,
# "linguagem" - 9. Usando um 'loop' for, imprima apenas as palavras cujo comprimento seja menor
# que o valor associado a elas.

palavras = {"python": 6, "programação": 12, "linguagem": 9}
for palavra in palavras.keys():
    if len(palavra) < palavras[palavra]:
        print(palavra)