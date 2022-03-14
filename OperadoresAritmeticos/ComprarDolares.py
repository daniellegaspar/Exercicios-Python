#Crie um programa que leia quando dinheiro uma pessoa tem na carteira e mostre quandos dólares ela pode comprar. ConsidereUS$1,00=R$3,27#
r = float(input('Quantos reais você tem? '))
uss = 5.07
c = r / uss
print('Você pode comprar US${:.2f} dólares com R${:.2f} reais.'.format(c, r))