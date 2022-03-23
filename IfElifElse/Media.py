'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no fial de acordo com a media atingida

media abaixo de 5.0 reprovado
media entre 5.0 e 6.9 recuperação
media 7.0 ou superior aprovado'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {} e você ficou abaixo da média. Você foi REPROVADO!'.format(media))
elif 7 > media >= 5:
    print("Sua média foi {} e você está de RECUPERAÇÃO!".format(media))
elif media >= 7:
    print('Sua média foi {}. Você está APROVADO! PARABÉNS!!'.format(media))

