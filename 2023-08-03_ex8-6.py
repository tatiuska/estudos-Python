#Reescreva o programa 8.2 de forma a utilizar for ao invés de while

def somar(l):
    total = 0
    for n in l:
        total += n
    return total

l = [20, 40, 50, 157, 239]

print(somar(l))