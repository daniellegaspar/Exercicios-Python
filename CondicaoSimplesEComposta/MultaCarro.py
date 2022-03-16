'''Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custas R$7,00 por cada km acima do limite.'''

vel = float(input('Você estava dirigindo em que velocidade?'))
if vel > 80:
    mul = (vel-80) * 7
    print('Você estava a {}km/h e foi multado, terá que pegar R${:.2f} de multa!'.format(vel, mul))
print('Dirija com cuidado. TENHA UM BOM DIA!')
