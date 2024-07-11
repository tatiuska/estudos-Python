from datetime import date, datetime
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from locacao import Locacao


# Classe Cliente e seus atributos
class Cliente:
    id: int
    nome: str
    data_nasc: date
    lista_locacao: List['Locacao']

    # Função de inicialização de um objeto da classe Cliente
    def __init__(self, nome: str, data_nasc: date) -> None:
        self.nome = nome
        self.data_nasc = data_nasc
        self.lista_locacao = []

    # Função que retorna os dados do cliente
    def __str__(self) -> str:
        return f"{self.nome} ({self.data_nasc:%d-%m-%Y}, {self.idade()} anos)"

    # Função para calcular a idade do cliente
    def idade(self) -> int:
        dif_data = (date.today() - self.data_nasc)
        return dif_data.days//365

    # Função para retornar a lista de filmes locados pelo cliente
    def get_locados(self) -> List['Locacao']:
        return list(filter(lambda x: x.locado, self.lista_locacao))
