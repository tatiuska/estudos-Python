from cliente import Cliente
from filme import Filme
from datetime import date, datetime
from locacao import Locacao
from exceptions import BlockbusterException
import service as service
from typing import List




#try:
# locacao1.devolver()
# print(f"Filmes locados por {cliente1.nome}: ")
# for loc in cliente1.lista_locacao:
#     print(f"\t {loc.data_locacao:%d-%m-%Y} {loc.filme}")
#
# print(f"Filmes locados por {cliente2.nome}: ")
# for loc in cliente2.lista_locacao:
#     print(f"\t {loc.data_locacao:%d-%m-%Y} {loc.filme}")
#
# print(f"Clientes que locaram {filme1.titulo}: ")
# for loc in filme1.lista_locacao:
#     print(f"\t {loc.data_locacao:%d-%m-%Y} {loc.cliente}")



# regra de atraso (saber se um filme está atrasado) - dt loc/dt dev hj+x) - data de registro do filme na locadora??
# nao permitir locacao quando atrasado
# mostrar quais filmes estão em atraso
# na exception do atraso, mostrar quais filmes estão em atraso

clientes: List[Cliente] = []
filmes: List[Filme] = []

# Criando Menu
nome_locadora = "LOCADORA JUVEVE"
print("|", "*", "|", "*", "|", "*", "|",  "*", "|", "*", "|", "*", "|", "*", "|")  # tirei o len(nome_locadora), pois só printava o número de caracteres da variável.
print("|", "*", "|", nome_locadora, " ", "|", "*", "|")
print("|", "*", "|", "*", "|", "*", "|", "*", "|", "*", "|", "*", "|", "*", "|")

while True:
    print("OPCOES:")
    print("[1] CADASTRAR FILME")
    print("[2] CADASTRAR CLIENTE")
    print("[3] LOCAR FILME")
    print("[4] DEVOLVER FILME")
    print("[5] CONSULTAR FILME")
    print("[6] CONSULTAR CLIENTE")
    print("[7] ENCERRAR ATENDIMENTO")

    opcao = input("Digite a opção desejada: ")

    # Opção 0: Encerrar o programa (mas o 7 não seria pra isso?)
    if opcao == "0":
        break

    # Opção 1 do Menu: Cadastrar Filme
    elif opcao == "1":
        try:
            nome_filme = input("Nome do filme: ")
            ano_lancamento = int(input("Ano de lançamento (aaaa): "))
            idade_minima = int(input("Idade mínima: (0/10/12/14/16/18) "))
            qtde_copias = int(input("Quantidade de cópias: "))
        except ValueError:
            print("dados inválidos, tente novamente.")
        else:
            filme = Filme(nome_filme, ano_lancamento, idade_minima, qtde_copias)
            filmes.append(filme)
            print(filme)

    # Opção 2 do Menu: Cadastrar Cliente
    elif opcao == "2":
        nome_cliente = input("Digite seu nome completo: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        datahora = datetime.strptime(data_nascimento, "%d/%m/%Y")
        cliente = service.criar_cliente(nome_cliente, datahora.date())
        clientes.append(cliente)
        print(cliente)

    # Opção 3 do Menu: Locar Filme
    elif opcao == "3":
        for i, elemento_filme in enumerate(filmes):
            print(i, elemento_filme)
        idx_filme = "-1"
        while not(idx_filme.isdigit() and 0 <= int(idx_filme) < len(filmes)):
            idx_filme = input(f"Escolha um filme entre 0 e {len(filmes)-1}: ")
        filme_selecionado = filmes[int(idx_filme)]

        for i, elemento_cliente in enumerate(clientes):
            print(i, elemento_cliente)
        idx_cliente = "-1"
        while not(idx_cliente.isdigit() and 0 <= int(idx_cliente) < len(clientes)):
            idx_cliente = input(f"Escolha um cliente entre 0 e {len(clientes)-1}: ")
        cliente_selecionado = clientes[int(idx_cliente)]

        try:
            locacao = Locacao(cliente=cliente_selecionado, filme=filme_selecionado)
            locacao.locar()
            print(locacao)
        except BlockbusterException as ex:
            print(ex)

    # Opção 4 do Menu: Devolver Filme
    elif opcao == "4":
        for i, elemento_cliente in enumerate(clientes):
            print(i, elemento_cliente)
        idx_cliente = "-1"
        while not(idx_cliente.isdigit() and 0 <= int(idx_cliente) < len(clientes)):
            idx_cliente = input(f"Escolha um cliente entre 0 e {len(clientes)-1}: ")
        cliente_selecionado = clientes[int(idx_cliente)]

        locacoes = cliente_selecionado.get_locados()

        for i, locacao in enumerate(locacoes):
            print(locacao.filme)
        idx_locacao = "-1"
        while not(idx_locacao.isdigit() and 0 <= int(idx_locacao) < len(locacoes)):
            idx_locacao = input(f"Escolha um filme entre 0 e {len(locacoes) - 1}: ")
        locacao_sel = locacoes[int(idx_locacao)]
        locacao_sel.devolver()

    elif opcao == "5":
        palavra_busca = input("Digite a palavra para buscar: ")
        achados = list(filter(lambda x: palavra_busca in x.titulo.lower() or x.ano.lower(), filmes))
        for filme in achados:
            print(filme)

    elif opcao == "6":
        palavra_busca = input("Digite o nome do cliente: ")
        achados = list(filter(lambda x: palavra_busca in x.nome.lower(), clientes))
        for cliente in achados:
            print(cliente)

    else:
        print("Opção não encontrada!")
