from cliente import Cliente
from datetime import date


# Função para criação de um Cliente no sistema da locadora
def criar_cliente(nome_cliente: str, data_nascimento: date) -> Cliente:
    cliente = Cliente(nome_cliente, data_nascimento)
    return cliente
