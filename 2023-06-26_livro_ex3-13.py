# Exercício 3.13: Escreva um programa que converta uma temperatura digitada em C em F.
# Dados de entrada
tempc = float(input("Digite uma temperatura em graus Celsius (C): "))

# Processamento
tempf = ((9 * tempc)/5) + 32

#Dados de saída
print(f"{tempc} C equivale a {tempf} F.")