numeros =[[], []]

for pos in range(1, 8):
    numero = int(input(f'Digite o {pos}o. valor: '))
    
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
print('Os valores pares digitados foram: ', end='')
for par in numeros[0]:
    if par == numeros[0][len(numeros[0]) - 1]:
        print(f'{par}.')
    else:
        print(par, end=', ')

numeros[1].sort()
print('Os valores ímpares digitados foram: ', end='')
for impar in numeros[1]:
    if impar == numeros[1][len(numeros[1]) - 1]:
        print(f'{impar}.')
    else:
        print(impar, end=', ')
