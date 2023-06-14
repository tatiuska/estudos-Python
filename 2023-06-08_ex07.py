# Exercício 7:
# Crie um dicionário chamado "agenda" com os seguintes pares de chaves e valores: "Ana" - "555-1234",
# "Maria" - "555-5678", "João" - "555-9876". Solicite ao usuário que digite um nome e, em seguida, verifique se o
# nome está presente na agenda. Se estiver, imprima o número de telefone correspondente; caso contrário, exiba uma
# mensagem informando que o nome não foi encontrado.

agenda = {'Ana': '555-1234', 'Maria': '555-5678', 'João': '555-9876'}
nome = input("Digite um nome: ")
if nome in agenda.keys():
    print(f"{agenda[nome]}")
else:
    print("Nome não encontrado!")
