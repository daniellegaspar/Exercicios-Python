'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
pc = randint(0, 5) # faz o computador sortear
print('=--' * 20)
print('Vou pensar em um número de 0 a 5 tente adivinhar!')
print('=--' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('EU GANHEI! Pensei no número {} e não no número {}!'.format(pc, jogador))