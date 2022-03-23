'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
conv = str(input('''Escolha uma das bases para conversão: 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL'''))
opcao = int(input('Sua opçao:'))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL fica {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL fica {}'.format(num, hex(num)[2:]))
else:
    print('==-==-== OPÇÃO INVÁLIDA! Tente novamente. ==-==-==')

