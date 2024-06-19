# Exercício 10: Classe Livro
# Crie uma classe chamada Livro com os atributos titulo e autor. Adicione um método descricao que
# imprime uma mensagem com o título e o autor do livro.

# classe Livro:
class Livro:
    titulo: str
    autor: str

    # Função de inicialização da classe Livro:
    def __init__(self, titulo: str, autor: str) -> None:
        self.titulo = titulo
        self.autor = autor


def descricao():
    titulo = input("Insira o título do livro: ")
    autor = input("Insira o nome do autor: ")
    return print(f"Título do livro: {titulo} - Autor(a): {autor}")

descricao()