# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
s1 = "a, b, c, d, e, f, g"
s2 = "g, f, d, c, b"
s3 = []
for letra in s2:
    if letra in s1:
        s3.append(letra)
s3 = "".join(s3)
print(s3)