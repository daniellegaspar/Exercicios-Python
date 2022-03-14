#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario com 15% de aumento.#
nome = str(input('Nome do Funcionário: '))
sa = float(input('Digite o salário antigo: '))
ns = sa + (sa * 15 / 100)
print('O novo salário do funcionário(a) {} é R${:.2f} reais'.format(nome, ns))
