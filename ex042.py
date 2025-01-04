#Pedindo o valor das vaiáveis
a = float(input('Cumprimento do segmento um: '))
b = float(input('Cumprimento do segmento dois: '))
c = float(input('Cumprimento do segmento três: '))

#Estrututa Condicional Aninhada
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo', end = ' ')
    if a == b and a == c:
        print('EQUILÁTERO.')
    elif a != b and a != c:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os segmentos acima não podem formar um triângulo!')
