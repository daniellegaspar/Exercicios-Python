'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo
abaixo de 18,5 abaixo do peso
entre 18.5 e 25 peso ideal
25 ate 30 sobrepeso
30 ate 40 obesidade
acima de 40 obesidade morbida'''

peso = float(input('Qual seu peso? KG '))
alt = float(input('Qual sua altura? '))
imc = peso / (alt ** 2)
print('=-=' * 8)
print('   Seu IMC é de {:.2f}'.format(imc))
print('=-=' * 8)
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso. Hora de consultar um nutricionista')
elif 30 <= imc < 40:
    print('Você está obeso. Hora de consultar um médico')
elif imc >= 40:
    print('Você está com obesidade mórbida. Hora de procurar um médico!')
