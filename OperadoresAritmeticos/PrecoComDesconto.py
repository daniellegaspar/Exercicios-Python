#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.#
preco = float(input("Qual o valor do produto? R$"))
novo = preco - (preco * 5 / 100)
print('O valor do produto com desconto será de R${:.2f} reais'.format(novo))