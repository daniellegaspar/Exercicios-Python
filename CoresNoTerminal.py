# -===-===-===-  Padrão ANSI (escape sequence)  -===-===-===-

# Sempre que quiser colocar uma cor em python iniciamos com \033[0;33;44m]
'''
|    Style    |    Text     |   Background  |
|0 nenhum     |30 branco    |40 branco      |
|1 negrito    |31 vermelho  |41 vermelho    |
|4 sublinhado |32 verde     |42 verde       |
|7 negativo   |33 amarelo   |43 amarelo     |
|             |34 azul      |44 azul        |
|             |35 roxo      |45 roxo        |
|             |36 verde água|46 verde água  |
|             |37 cinza     |47 cinza       |
'''

print('\033[7;34;40mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))

nome = 'Danielle'
print('Olá! Bom te conhecer, {}{}{}!!!'.format('\033[4;36m', nome, '\033[m'))

# Criar lista de cores para utilizar (dicionário)
nome = 'Danielle'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Bom te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

