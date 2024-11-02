from random import choices

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
aleatorios = (choices(numeros, k = 5))
print(f'Os valores sorteados foram: {aleatorios}')

if int(aleatorios[0]) > int(aleatorios[1:]):
    print(f'O menor valor é {aleatorios[0]}')