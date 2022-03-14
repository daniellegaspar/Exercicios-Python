# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite o Nome Completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper())) # O nome com todas as letras maiúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower())) # O nome com todas minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # Quantas letras ao todo sem considerar espaços
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) # Quantas letras tem o primeiro nome