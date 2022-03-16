'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
'''

num = int(input('Digite um número: '))
print('O número {} é par!'.format(num) if num % 2 == 0 else 'O número {} é impar!'.format(num))