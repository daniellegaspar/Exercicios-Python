# Tabuada de um número que o usuário escolher, utilizando o laço FOR

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 13)
print('TABUADA DO {}'.format(num))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-' * 13)
