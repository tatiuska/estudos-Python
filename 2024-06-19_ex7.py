# Exercício 7: Classe Retangulo
# Crie uma classe chamada Retangulo com os atributos largura e altura. Adicione métodos para calcular a área e o
# perímetro do retângulo.

# classe Retângulo
class Retangulo:

    # Inicialização da classe Retângulo
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura

    # Método para cálculo da área
    def area(self):
        return self.largura * self.altura

    # Método para cálculo do perímetro
    def perimetro(self):
        return (self.largura + self.altura) * 2


# Instanciação da classe Retângulo
calculo = Retangulo(10, 4)
print(calculo.area())
print(calculo.perimetro())
