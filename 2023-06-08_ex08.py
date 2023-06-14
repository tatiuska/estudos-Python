# Exercício 8:
# Crie um dicionário chamado "notas" com os seguintes pares de chaves e valores: "João" - [7, 8, 9],
# "Maria" - [6, 7, 8], "Pedro" - [9, 9, 10]. Utilizando um 'loop' for, calcule
# e imprima a média das notas de cada aluno.

notas = {"João": [7, 8, 9], "Maria": [6, 7, 8], "Pedro": [9, 9, 10]}
for aluno, notas_aluno in notas.items():
    soma_aluno = 0
    for nota in notas_aluno:
        soma_aluno += nota
    media = soma_aluno / len(notas_aluno)
    print(f"{aluno} - Média: {media:.2f}")