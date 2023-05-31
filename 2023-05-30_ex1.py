#Escreva um programa que leia nomes de alunos e suas respectivas notas até que o nome 'oooo' seja informado.
#Após o fim da leitura, imprima o nome do aluno que possui a maior nota. Use o dicionário.
notas = {}
while True:
    nome = input("Digite o nome da fera: ").title()
    if nome == "Oooo":
        break
    else:
        nota = float(input("Digite a nota do aluno: "))
        notas[nome] = nota

#Inicializando as variáveis
maior_nota = 0
aluno_maior_nota = ""

for x, y in notas.items():
    if y >= maior_nota:
        maior_nota = y
        aluno_maior_nota = x

print(f"A fera com a maior nota é: " + aluno_maior_nota, maior_nota)
