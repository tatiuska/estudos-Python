from datetime import date, datetime, timedelta
from filme import Filme
from cliente import Cliente
from exceptions import BlockbusterException, ExceptionCodes
from settings import PRECO_CATALOGO, PRECO_LANCAMENTO, QTDE_MAX, PRAZO_LANCAMENTO, PRAZO_CATALOGO


# Classe Locação e seus atributos
class Locacao:
    id: int
    data_locacao: datetime
    data_devolucao: datetime
    filme: Filme
    cliente: Cliente
    locado: bool = False
    lancamento: bool
    preco: int

    def __init__(self, filme: Filme, cliente: Cliente, lancamento: bool = False) -> None:
        self.data_locacao = datetime.now()
        self.filme = filme
        self.cliente = cliente
        self.lancamento = lancamento
        self.preco = PRECO_LANCAMENTO if self.lancamento else PRECO_CATALOGO
        prazo = PRAZO_LANCAMENTO if self.lancamento else PRAZO_CATALOGO
        self.data_devolucao = self.data_locacao + timedelta(days=prazo)
        # if self.lancamento: self.preco = PRECO_LANCAMENTO
        # else: self.preco = PRECO_CATALOGO

    # Validação da idade do cliente para locar filmes de acordo com sua classificação
    def validar_data_nasc(self) -> None:
        if self.filme.classif > self.cliente.idade():
            raise BlockbusterException(ExceptionCodes.V01)

    # Função para validar se um filme locado está em atraso
    def validar_existe_atrasos(self) -> None:
        for loc in self.cliente.get_locados():
            print(self.cliente, loc.data_devolucao, datetime.now())
            if loc.data_devolucao < datetime.now():
                raise BlockbusterException(ExceptionCodes.A01)

    # Método de validação da quantidade de filmes disponíveis na locadora
    def validar_qtde(self) -> None:
        if self.filme.qtde < 1:
            raise BlockbusterException(ExceptionCodes.V02)

    # Método de validação da quantidade máxima de filmes que o cliente pode locar
    def validar_qtde_max(self) -> None:
        if len(self.cliente.get_locados()) > QTDE_MAX:
            raise BlockbusterException(ExceptionCodes.V03)

    # Método de validação de filme para locação com base na idade do cliente
    def validar_locado(self) -> None:
        if not self.locado:
            raise BlockbusterException(ExceptionCodes.L01)

    # Método para retornar as informações de confirmação da locação
    def __str__(self) -> str:
        return f"{self.data_locacao:%d-%m-%Y %H:%m}: {self.cliente.nome} -> {self.filme.titulo} -> R$ {self.preco/100:.2f}"

    # Função para locar um filme
    def locar(self) -> None:
        self.validar_data_nasc()
        self.validar_existe_atrasos()
        self.validar_qtde()
        self.validar_qtde_max()
        self.cliente.lista_locacao.append(self)
        self.filme.lista_locacao.append(self)
        self.filme.qtde -= 1
        self.locado = True

    # Função para devolver um filme
    def devolver(self) -> None:
        self.validar_locado()

        self.filme.qtde += 1
        self.locado = False
