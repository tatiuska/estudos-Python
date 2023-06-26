# Exercício 3.12: Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input("Informe a distância a ser percorrida (em km): "))
vm = int(input("Informe a velocidade média (em km/h): "))
tempo = dist / vm

print(f"Sua viagem de carro terá duração de {tempo} h.")