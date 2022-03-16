'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
 Km para viagens de até 200Km e R$0,45 para viagens mais longas'''

from time import sleep
km = float(input('Qual a distância da sua viagem? Km '))
pas = (km * 0.5)
passa = (km * 0.45)
print('=--=' * 20)
print('Você está prestes a iniciar uma viagem de {}Km.'.format(km))
print('=--=' * 20)
print('Calculando...')
sleep(2)
if km <= 200:
    print('O preço de sua passagem é de R${:.2f}'.format(pas))
else:
    print('O valor de sua passagem é de R${:.2f}'.format(passa))

