'''A confederação NAcional de natação precisa de um programa que leia o ano
 de nascimento de um atleta e mostre sua
categoria de acordo com a idade

ate 9 anos mirim
ate 14 infantil
ate 19 junior
ate 25 senior
acima master'''

from datetime import date
atual = date.today().year
ano_nasc = int(input('Qual ano de nascimento do atleta? '))
idade = atual - ano_nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
elif idade > 25:
    print('Categoria MASTER')
