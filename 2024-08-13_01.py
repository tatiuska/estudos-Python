# Exercício 5: Votação Elegível
# Peça ao usuário para inserir sua idade e nacionalidade, e verifique se ele é elegível para votar (18 anos ou mais e nacionalidade "brasileira").

def votacao():
    idade = int(input("Informe sua idade: "))
    nacionalidade = input("Informe sua nacionalidade: ")
    titulo = bool(input("Possui título de eleitor? "))

    if(idade >= 16) and (nacionalidade == "Brasileiro") and (titulo == True):
        print("Você é elegível para votar. ")
    
    else: {
        print("Você não é elegível para votar. ")
    }
        
    
votacao()