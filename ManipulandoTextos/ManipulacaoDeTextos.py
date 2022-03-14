# MANIPULANDO CADEIAS DE TEXTO

# FATIAMENTO
frase = 'Curso de Python'
print(frase[9])
print(frase[9:15])
print(frase[9:15:2])
print(frase[:5])
print(frase[9:])
print(frase[9::3])


# ANÁLISE
print(len(frase)) # comprimento
print(frase.count('o')) # vai contar quantas vezes a letra o aparece (letra o minúscula)
print(frase.count('o', 0, 13)) # conta quantas vezes aparece a letra o e o fatiamento
print(frase.find('de')) # encontra a palavra e em que momento/posição ela começou
print(frase.rfind('de')) # encontra a palavra e em que momento/posição ela terminou
print('Curso' in frase) # verifica se existe a palavra dentro da frase e retorna True ou False


# TRANSFORMAÇÃO
print(frase.replace('Pyhton', 'Android'))# tocar/reposicionar
print(frase.upper())# Letras maiúsculas
print(frase.lower())# Letras minúsculas
print(frase.capitalize())# Deixa apenas a primeira letra maiúscula e o restante minúsculo
print(frase.title())# Deixa a primeira letra de cada palavra maiúscula e o restante minúscula
print(frase.strip())# Remove os espaços inúteis das extremidades
print(frase.rstrip())# Remove os espaços da direita/final
print(frase.lstrip())# Remove os espaços da esquerda/inicio


# DIVISÃO
print(frase.split())# Faz uma divisão na string considerando os espaços e gera novos índices
#Ex:
dividido = frase.split()
print(dividido[2]) # Dividido 2 é Python

dividido = frase.split()
print(dividido[2][3]) # Dividido 2 e a letra 3 = h


# JUNÇÃO
print('-'.join(frase)) # vai juntar os elementos em uma única string usando o separador -
