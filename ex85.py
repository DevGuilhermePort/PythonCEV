numeros = [[],[]]

for i in range (1, 8):
    numero = int(input(f'Digite o {i}o. valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f'Os valores pares digitados foram: {sorted(numeros[0])}.')
print(f'Os calores ímpares digitados foram: {sorted(numeros[1])}.')
