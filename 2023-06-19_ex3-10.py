# Exercício 3.10: faça um programa que calcule o aumento de um salário.
# Deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

# Variáveis e dados de entrada
salario = input("Informe o valor do seu salário: ")
porcentagem = input("Informe a porcentagem do aumento: ")

# Processamento
aumento = float(salario) * float(porcentagem)
novo_salario = float(salario) + float(aumento)

# Dados de saída
print(f"Para o salário de {salario}, o valor do aumento será de {aumento}.")
print(f"Seu novo salário será no valor de {novo_salario}")
