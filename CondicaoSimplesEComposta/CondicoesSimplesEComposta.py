# CONDIÇÕES SIMPLES E COMPOSTA

# Estrutura condicional: IF e ELSE
EX:
carro.siga()
if carro.esquerda():
    blocoTrue
    carro.siga()
    ...
    ...
    ...
else:
    blocoFalse
    carro.siga()
    carro.esquerda()
    ...
    ...
    ...
carro.pare()

=================================================

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')

=================================================

# Condição Simplificada
tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('---FIM---')

'''Todo comando que estiver colado do lado esquerdo da tela será sempre executado, e o que estiver aninhado/indentado vai ser executado ou não dependendo da situação.'''




