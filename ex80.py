numeros = []

for cont in range(0, 5):
    numero = int(input('Digite um valor: '))

    if cont == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista.')
        print()
    
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                print(f'Adicionado na posição {pos}.')
                print()
                break
            pos += 1

print(f'Números digitados: {numeros}')
