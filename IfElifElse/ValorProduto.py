'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento

a vista dinheiro/cheuque 10% desconto
a vista no cartao 5% desconto
em ate 2x cartão preço normal
3x ou mais no cartão 20% juros'''

print('===' * 12)
valorpro = float(input('    Preço das compras? R$ '))
print('''FORMAS DE PAGAMENTO
[ 0 ] A vista Dinheiro/Cheque
[ 1 ] A vista no cartão
[ 2 ] Parcelado em 2x no cartão
[ 3 ] Parcelado em 3x ou mais no cartão''')
cliente = int(input('Escolha uma opção: '))
print('Você escolheu a opção {}'.format(cliente))
if cliente == 0:
    desc10 = valorpro - (valorpro * 10 / 100)
    print('Você iría pagar sem desconto R${:.2f} e com desconto de 10% você irá pagar R${:.2f}'.format(valorpro, desc10))
elif cliente == 1:
    desc5 = valorpro - (valorpro * 5 / 100)
    print('Você iría pagar sem desconto R${:.2f} e com desconto de 5% você irá pagar R${:.2f}'.format(valorpro, desc5))
elif cliente == 2:
    parc2x = valorpro / 2
    print('Você irá pagar R${:.2f} em 2x SEM JUROS de {:.2f}'.format(valorpro, parc2x))
elif cliente == 3:
    total = valorpro + (valorpro * 20 / 100)
    totparc = int(input('Qual número de parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = valorpro
    print('Opção Inválida de pagamento. Tente novamente!')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valorpro, total))
