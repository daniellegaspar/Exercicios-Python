'''Refaça o desafio dos triangulos acrescentando o recurso de
mostrar qual tipo de triangulo
sera formado
equilatero
isosceles
escaleno'''

print('-=-=' * 12)
print('          Analisador Tipo de Triângulos')
print('-=-=' * 12)
ladosIguais = int(input('Quantos lados iguais seu triângulo tem? '))
if ladosIguais == 3:
    print('É um triângulo Equilátero!')
elif ladosIguais ==2:
    print('É um triângulo Isósceles!')
else:
    print('É um triângulo Escaleno')