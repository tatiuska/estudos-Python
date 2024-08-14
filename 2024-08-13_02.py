# Exercício 2: Verificação de Faixa e Estado
# Peça ao usuário para inserir um número e verifique se ele está na faixa de 10 a 50, inclusive e se o estado é "RJ".

def verificar():
    numero = int(input("Insira um número: "))
    estado = input("Informe seu Estado: ")

    if numero == 10 or numero <= 50 and estado == "RJ":
        print("Sim")

    else: 
        print("Não")


verificar()