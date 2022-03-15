'''EX 1:
nome = str(input('Qual é o seu nome? '))
if nome == 'Danielle':
    print('Bom dia!') # esse bloco só vai acontecer se o nome for "Danielle"
print('Seja bem-vinda(o) aqui {}!'.format(nome)) # Esse bloco sempre vai acontecer'''

'''Quando temos apenas a estrutura IF é uma estrutura simples, e, quando temos o IF e o ELSE é uma estrutura composta'''

'''EX 2:'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1+nota2)/2
print('A sua média foi'.format(m))
print('PARABÉNS!!!' if m>=6.0 else 'ESTUDE MAIS!')
