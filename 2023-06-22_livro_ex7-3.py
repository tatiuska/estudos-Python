# Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
s1 = "CTA"
s2 = "ABC"
s3 = ""
for i in s1:
    if i not in s2 and i not in s3:
        s3 += i

for i in s2:
    if i not in s1 and i not in s3:
        s3 += i
print(s3)