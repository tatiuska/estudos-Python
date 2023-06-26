# Exercício 3.14: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, e quantidade de dias de aluguel do carro.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

km = float(input("Digite quantos quilômetros percorrer com o carro: "))
dias = int(input("Informe por quantos dias esteve com o carro: "))
diaria = dias * 60
kms = km * 0.15
total = diaria + kms
print(f"O total a pagar por {km} kms rodados em {dias} dias será de: {total:5.2f}")