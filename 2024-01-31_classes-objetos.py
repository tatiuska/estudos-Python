# Objetos como representação do mundo real
# criando classe Televisao e instanciando com dois atributos ligada e canal
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2


# criação do objeto tv por meio da classe Televisao
tv = Televisao()
print(tv.ligada)
print(tv.canal)

# criação do objeto tv_quarto e mudança de valores para os atributos ligada e canal
tv_quarto = Televisao()
tv_quarto.ligada = True
tv_quarto.canal = 4
print(tv.canal)
print(tv_quarto.canal)
