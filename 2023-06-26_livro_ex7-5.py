# Exercício 7.6: Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira
s1 = "AATTGGAA"
s2 = "TG"
s3 = ""

for i in s1:
    if i in s1 and i not in s2:
        s3 += i
print(s3)