numeros = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]

    if continuar == 'n':
        break

print('A lisca completa é: ', end='')
for numero in numeros:
    if numero == numeros[-1]:
        print(numero, end='.\n')
    else:
        print(numero, end=', ')

print('A lista de pares é: ', end='')
for par in pares:
    if par == pares[-1]:
        print(par, end='.\n')
    else:
        print(par, end=', ')

print('A lista de ímpares é: ', end='')
for impar in impares:
    if impar == impares[-1]:
        print(impar, end='.\n')
    else:
        print(impar, end=', ')
