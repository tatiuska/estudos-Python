# Exercício 3.15: Escreva um programa que calcule a redução de tempo de vida de um fumante.
# Pergunte a quantidade de cigarros por dia e quantos anos já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
#Dados de entrada
cigs_dia = int(input("Informe quantos cigarros você fuma por dia: "))
anos_fumante = int(input("Informe por quantos anos você já fumou: "))

# Processamento
dias = 365 * anos_fumante
cigs_total = cigs_dia * dias
minutos_perdidos = dias * 1440
dias_vida = (cigs_total * 10) / 1440

# Dados de saída
print(f"Você já perdeu {dias_vida} dias de vida.")