# Exercício 7.6: Escreva um programa que leia duas strings.
# Imprima o resultado da substituição na primeira, dos caracteres na segunda pelos da terceira.
s1 = "AATTCGAA"
s2 = "TG"
s3 = "AC"
if len(s2) == len(s3):
    resultado = ""
    for i in s1:
        pos = s2.find(i)
        if pos != -1:
            resultado += s3[pos]
        else:
            resultado += i
print(f"Resultado: {resultado}")