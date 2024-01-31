# Adicione os atributos tamanho e marca à classe Televisão.
# Crie dois objetos Televisao e atribua tamanhos e marcas diferentes.
# Imprima o valor desses atributos de forma a confirmar a independência de valores de cada instância.

# Criando classe Televisao
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = "43 polegadas"
        self.marca = "Samsung"


# criando objeto tv, que terá os valores dos atributos originalmente instanciados na classe Televisao
tv = Televisao()
print(f"Esta televisão possui {tv.tamanho}, e é da marca {tv.marca}. Foi sintonizada no canal {tv.canal}. "
      f"Está ligada? {tv.ligada}.")

# criando objeto tv_sala e mudando os valores dos atributos
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala_tamanho = "60 polegadas"
tv_sala.marca = "Philco"
print(f"A televisão da sala é da marca {tv_sala.marca} e possui {tv_sala.tamanho}. "
      f"Está sintonizada no canal {tv_sala.canal}. Está ligada? {tv_sala.ligada}.")

# criando objeto tv_cozinha com outros valores de atributos
tv_cozinha = Televisao()
tv_cozinha.tamanho = "10 polegadas"
tv_cozinha.marca = "LG"
print(f"Já a televisão da cozinha é de {tv_cozinha.tamanho}, da marca {tv_cozinha.marca}.")
