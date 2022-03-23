l1 = float(input('Primeiro Segmento: '))
l2 = float(input('Segundo Segmento: '))
l3 = float(input('Terceiro Segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguimentos acima podem formar um triângulo ')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem formar um triângulo!')
