from enum import Enum


# Classe Enum com as mensagens dos códigos de exceção
class ExceptionCodes(Enum):
    V01 = "Filme Inaprorpiado."
    V02 = "Quantidade Indisponível."
    V03 = "Quantidade máxima de filmes locados atingida."
    L01 = "O filme não está contigo para ser devolvido!!!"
    A01 = "Existe(m) filme(s) em atraso!!"


# Classe de exceções referentes às regras de negócio
class BlockbusterException(Exception):
    codigo: str
    mensagem: str

    def __init__(self, code: ExceptionCodes) -> None:
        super().__init__(code.value)

        self.codigo = code.name
        self.mensagem = code.value

    def __str__(self) -> str:
        return f'{self.codigo}: {self.mensagem}'
