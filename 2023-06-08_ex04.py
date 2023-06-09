# Exercício 4:
# Crie um dicionário chamado "alunos" com as seguintes chaves e valores: "João" - 8, "Maria" - 9, "Pedro" - 7.
# Utilizando um loop for, calcule e imprima a média das notas dos alunos.

alunos = {"João": 8, "Maria": 9, "Pedro": 7}
media = 0
for nota in alunos.values():
    media = media + nota / 3
print(f"{media:.2f}")