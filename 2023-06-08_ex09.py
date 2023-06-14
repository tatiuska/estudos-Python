# Exercício 9:
# Crie um dicionário chamado "estoque" com as seguintes chaves e valores: "camisetas" - 10, "calças" - 15,
# "sapatos" - 20. Solicite ao usuário que digite o nome de um item e a quantidade desejada. Em seguida, verifique se o
# item existe no estoque e se há a quantidade solicitada disponível. Se estiver, atualize o estoque subtraindo a
# quantidade desejada; caso contrário, exiba uma mensagem informando que o item não está disponível ou que a quantidade
# desejada não está disponível.

estoque = {"camisetas": 10, "calças": 15, "sapatos": 20}
nome = input("Digite o item desejado: ")
if nome in estoque:
    qtd = int(input("Digite a quantidade desejada: "))
    if qtd <= estoque[nome]:
        print(f"{nome} em estoque: {estoque[nome] - qtd}")
    else:
        print("Item não está disponível")