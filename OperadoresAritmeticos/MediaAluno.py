#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média#
n = str(input('Nome do Aluno: '))
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2
print('A média do(a) aluno(a) {} é {}'.format(n, m))
