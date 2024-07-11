from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from locacao import Locacao


# Classe Filme e seus atributos
class Filme:
    id: int
    titulo: str
    ano: int
    classif: int
    lista_locacao: List['Locacao']
    qtde: int
    qtde_max: int

    def __init__(self, titulo: str, ano: int, classif: int, qtde: int = 1) -> None:
        self.titulo = titulo
        self.ano = ano
        self.classif = classif
        self.lista_locacao = []
        self.qtde = qtde
        self.qtde_max = qtde


    def __str__(self) -> str:
        return f"[{self.qtde}/{self.qtde_max}] {self.titulo}, {self.ano} ({self.classif} anos)"


# criar uma máquina de estados para qtde de filmes locados.
# duas variáveis, uma qtde total e outra qtde disponíveis
