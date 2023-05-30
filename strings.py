#Capítulo 3.4 - Variáveis string
#Uso da função len()
print("Número de caracteres na string 'A':", len("A"))
print("Número de caracteres na string 'AB':", len("AB"))
print("Número de caracteres na string vazia:", len(""))
print("Número de caracteres na string 'O rato roeu a roupa':", len("O rato roeu a roupa"))

#Testes com strings
a = "ABCDEF"
print("Na string 'ABCDE', o caracter no índice 0 é:", a[0])
print("Na string 'ABCDE', o caracter no índice 1 é:", a[1])
print("Na string 'ABCDE', o caracter no índice 5 é:", a[5])
print("Na string 'ABCDE', o caracter no índice 6 é:", a[6]) #Aqui vai dar erro
print("O tamanho da string 'ABCDEF' é:", len(a))