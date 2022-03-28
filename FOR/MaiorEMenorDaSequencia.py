'''Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.'''

maiorpeso = 0
menorpeso = 0
for p in range(1, 6):
    peso = float(input('Qual peso da {}ª pessoa? KG '.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi {}Kg'.format(maiorpeso))
print('O menor peso lido foi {}Kg'.format(menorpeso))