'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que o ajude, lendo o nome deles e mostre a ordem sorteada.'''

from random import shuffle
a1 = input('Qual nome do primeiro aluno? ')
a2 = input('Qual nome do segundo aluno? ')
a3 = input('Qual nome do terceiro aluno? ')
a4 = input('Qual nome do quarto aluno? ')
lista = [a1, a2, a3, a4]
sorteio = random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
