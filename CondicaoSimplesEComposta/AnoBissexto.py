'''Faça um programa que leia um ano qualquer e mostre se ele e bissexto'''

from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
print('O ano {} É BISSEXTO'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'O ano {} NÃO É BISSEXTO'.format(ano))
