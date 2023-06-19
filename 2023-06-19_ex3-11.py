# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

# Variáveis e dados de entrada
preco = input("Informe o valor da mercadoria: ")
percentual = input("Informe o percentual de desconto: ")

# Processamento
desconto = float(preco) * float(percentual)
preco_final = float(preco) - float(desconto)

# Dados de Saída
print(f"O valor do desconto será de R$ {desconto} e o preço a pagar será de R$ {preco_final}")