'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.'''

from random import choice
a1 = input('Qual nome do primeiro aluno? ')
a2 = input('Qual nome do segundo aluno? ')
a3 = input('Qual nome do terceiro aluno? ')
a4 = input('Qual nome do quarto aluno? ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno escolhido foi', sorteio)