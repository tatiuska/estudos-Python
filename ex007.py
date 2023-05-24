#Exercício 3.6: Escrever uma expressão para decidir se um aluno foi ou não aprovado
#Para ser considerado aprovado, todas as médias devem ser maiores do que 7
#Considere que o aluno cursa apenas três matérias e que a nota de cada uma seja armazenada nas variáveis materia1, materia2, materia3

materia1 = 7
materia2 = 8
materia3 = 6
if(materia1 and materia2 and materia3 >= 7):
    print("A nota da matéria 1 é", materia1, ", a nota da matéria 2 é", materia2, "e a nota da matéria 3 é", materia3)
    print("Aluno aprovado!")
else:
    print("A nota da matéria 1 é", materia1, ", a nota da matéria 2 é", materia2, "e a nota da matéria 3 é", materia3)
    print("Aluno reprovado!!")