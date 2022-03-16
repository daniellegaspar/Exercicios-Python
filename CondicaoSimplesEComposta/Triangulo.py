'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo'''

print('-=-=' * 12)
print('          Analisador de Triângulos')
print('-=-=' * 12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo!')

