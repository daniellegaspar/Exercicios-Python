#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possívis sobre ele#
valor = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(valor))
print('É alfanúmerico?', valor.isalnum())
print('É numérico?', valor.isnumeric())
print('É decimal?', valor.isdecimal())
print('É um espaço?', valor.isspace())

