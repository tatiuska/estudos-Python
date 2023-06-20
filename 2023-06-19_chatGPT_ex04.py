# Exercício 4:
# Crie um conjunto chamado "alunos" com nomes de alunos.
# Solicite ao usuário que digite o nome de um aluno e verifique se o aluno está presente no conjunto.
# Se estiver, imprima uma mensagem informando que o aluno foi encontrado; caso contrário, exiba uma mensagem informando que o aluno não foi encontrado.

alunos = {"Kramer", "Jerry", "Elaine", "Soup Nazi", "George"}
nome = input("Digite o nome de um aluno: ")

if nome in alunos:
    print(f"O aluno {nome} está presente no conjunto.")
else:
    print(f"O aluno {nome} não está presente no conjunto.")