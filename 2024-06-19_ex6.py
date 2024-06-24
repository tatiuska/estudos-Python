# Exercício 6: Classe Pessoa
# Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método apresentar que imprime uma mensagem
# com o nome e a idade da pessoa.

# Classe Pessoa
class Pessoa:

    # inicialização da classe Pessoa
    def __init__(self, nome: str, idade: str) -> None:
        self.nome = nome
        self.idade = idade

    # Método apresentar
    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"


# Instanciando a classe Pessoa
regi = Pessoa("Peter Parker", 17)
print(regi.apresentar())
